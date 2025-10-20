from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer

class Home(APIView):
    def get(self, request):
        return Response({"message": "Hello from Django backend!"})

class NotesIndex(APIView):
    serializer_class = NoteSerializer

    def get(self, request):
        queryset = Note.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
