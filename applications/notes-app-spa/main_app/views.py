from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import get_object_or_404

from .models import Note, MoodCheck, Photo, Reaction
from .serializers import (
    NoteSerializer,
    MoodCheckSerializer,
    PhotoSerializer,
    ReactionSerializer,
)


class Home(APIView):
    def get(self, request):
        return Response({"message": "Hello from Django backend!"})


class NotesIndex(APIView):
    serializer_class = NoteSerializer

    def get(self, request):
        queryset = Note.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetail(APIView):
    serializer_class = NoteSerializer
    lookup_field = "id"

    def get(self, request, note_id):
        try:
            note = get_object_or_404(Note, id=note_id)

            moodchecks = MoodCheck.objects.filter(note=note_id).order_by("-date")

            reactions_note_has = Reaction.objects.filter(notes=note_id)
            reactions_note_doesnt_have = Reaction.objects.exclude(
                id__in=note.reactions.all().values_list("id", flat=True)
            )

            return Response(
                {
                    "note": NoteSerializer(note).data,
                    "moodChecks": MoodCheckSerializer(moodchecks, many=True).data,
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


class MoodChecksIndex(APIView):
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
    serializer_class = ReactionSerializer
    queryset = Reaction.objects.all()


class ReactionDetail(APIView):
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
