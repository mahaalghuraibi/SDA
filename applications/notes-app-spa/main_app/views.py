from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from .models import Note, MoodCheck, Photo, Reaction
from .serializers import (
    NoteSerializer,
    MoodCheckSerializer,
    PhotoSerializer,
    ReactionSerializer,
    UserSerializer,
)


class Home(APIView):
    def get(self, request):
        return Response({"message": "Hello from Django backend!"})


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        }
        return Response(data, status=status.HTTP_201_CREATED)


class NotesIndex(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NoteSerializer

    def get(self, request):
        try:
            queryset = Note.objects.filter(user=request.user)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save(user_id=request.user.id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MoodChecksIndex(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MoodCheckSerializer

    def get(self, request, note_id):
        try:
            queryset = MoodCheck.objects.filter(note=note_id).order_by("-date")
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, note_id):
        try:
            note = get_object_or_404(Note, id=note_id)
            data = request.data.copy()
            data["note"] = note.id
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
                queryset = MoodCheck.objects.filter(note=note_id).order_by("-date")
                moodchecks = MoodCheckSerializer(queryset, many=True)
                return Response(moodchecks.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response({"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PhotoDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PhotoSerializer

    def post(self, request, note_id):
        try:
            data = request.data.copy()
            data["note"] = int(note_id)

            existing_photo = Photo.objects.filter(note=note_id)
            if existing_photo.exists():
                existing_photo.delete()

            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                note = get_object_or_404(Note, id=note_id)
                serializer.save()
                return Response(NoteSerializer(note).data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response({"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ReactionIndex(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReactionSerializer
    queryset = Reaction.objects.all()


class ReactionDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReactionSerializer
    lookup_field = "id"

    def get(self, request, reaction_id):
        try:
            reaction = get_object_or_404(Reaction, id=reaction_id)
            data = self.serializer_class(reaction).data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, reaction_id):
        try:
            reaction = get_object_or_404(Reaction, id=reaction_id)
            serializer = self.serializer_class(reaction, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response({"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, reaction_id):
        try:
            reaction = get_object_or_404(Reaction, id=reaction_id)
            reaction.delete()
            return Response({"success": True}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AddReactionToNote(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, note_id, reaction_id):
        try:
            note = get_object_or_404(Note, id=note_id)
            reaction = get_object_or_404(Reaction, id=reaction_id)

            note.reactions.add(reaction)

            reactions_note_has = Reaction.objects.filter(notes=note_id)
            reactions_note_doesnt_have = Reaction.objects.exclude(
                id__in=note.reactions.all().values_list("id", flat=True)
            )

            return Response(
                {
                    "reactionsNoteHas": ReactionSerializer(
                        reactions_note_has, many=True
                    ).data,
                    "reactionsNoteDoesntHave": ReactionSerializer(
                        reactions_note_doesnt_have, many=True
                    ).data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as err:
            return Response({"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RemoveReactionFromNote(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, note_id, reaction_id):
        try:
            note = get_object_or_404(Note, id=note_id)
            reaction = get_object_or_404(Reaction, id=reaction_id)

            note.reactions.remove(reaction)

            reactions_note_has = Reaction.objects.filter(notes=note_id)
            reactions_note_doesnt_have = Reaction.objects.exclude(
                id__in=note.reactions.all().values_list("id", flat=True)
            )

            return Response(
                {
                    "reactionsNoteHas": ReactionSerializer(
                        reactions_note_has, many=True
                    ).data,
                    "reactionsNoteDoesntHave": ReactionSerializer(
                        reactions_note_doesnt_have, many=True
                    ).data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as err:
            return Response({"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(APIView):
    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                content = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': UserSerializer(user).data
                }
                return Response(content, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VerifyUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            user = User.objects.get(username=request.user.username)
            try:
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'user': UserSerializer(user).data
                    },
                    status=status.HTTP_200_OK
                )
            except Exception as token_error:
                return Response(
                    {"detail": "Failed to generate token.", "error": str(token_error)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        except Exception as err:
            return Response(
                {"detail": "Unexpected error occurred.", "error": str(err)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class NoteDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NoteSerializer
    lookup_field = "id"

    def get(self, request, note_id):
        try:
            note = get_object_or_404(Note, id=note_id)
            return Response(NoteSerializer(note).data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, note_id):
        note = get_object_or_404(Note, id=note_id)
        serializer = self.serializer_class(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, note_id):
        note = get_object_or_404(Note, id=note_id)
        note.delete()
        return Response({"success": True}, status=status.HTTP_200_OK)
