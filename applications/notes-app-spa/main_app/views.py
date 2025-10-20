from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Note, MoodCheck, Photo           
from .serializers import NoteSerializer, MoodCheckSerializer, PhotoSerializer  


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
    lookup_field = 'id'

    def get(self, request, note_id):
        note = get_object_or_404(Note, id=note_id)
        data = self.serializer_class(note).data
        return Response(data, status=status.HTTP_200_OK)

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
        return Response({'success': True}, status=status.HTTP_200_OK)


class MoodChecksIndex(APIView):
    serializer_class = MoodCheckSerializer

    def get(self, request, note_id):
        try:
            queryset = MoodCheck.objects.filter(note=note_id).order_by('-date')
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, note_id):
        try:
            note = get_object_or_404(Note, id=note_id)
            data = request.data.copy()
            data['note'] = note.id

            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
                queryset = MoodCheck.objects.filter(note=note_id).order_by('-date')
                moodchecks = MoodCheckSerializer(queryset, many=True)
                return Response(moodchecks.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
