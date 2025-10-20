from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Cat
from .serializers import CatSerializer


# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the cat-collector api home route!'}
    return Response(content)


class Cats(APIView):
  def get(self, request):
    content = [
        {"name": 'Lolo', "breed": 'tabby', "description": 'Kinda rude.', "age": 3},
        {"name": 'Sachi', "breed": 'tortoiseshell', "description": 'Looks like a turtle.', "age": 0},
        {"name": 'Fancy', "breed": 'bombay', "description": 'Happy fluff ball.', "age": 4},
        {"name": 'Bonk', "breed": 'selkirk rex', "description": 'Meows loudly.', "age": 6},
    ]
    return Response(content)

class CatsIndex(APIView):
  serializer_class = CatSerializer

  def get(self, request):
    try:
      queryset = Cat.objects.all()
      serializer = self.serializer_class(queryset, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  def post(self, request, *args, **kwargs):
    try:
      serializer = self.serializer_class(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CatDetail(APIView):
  serializer_class = CatSerializer
  lookup_field = 'id'

  def get(self, request, cat_id):
    try:
      queryset = Cat.objects.get(id=cat_id)
      cat = CatSerializer(queryset)
      return Response(cat.data, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)   
