from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Cat, Feeding, Photo, Toy
from .serializers import CatSerializer, FeedingSerializer, PhotoSerializer, ToySerializer


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
            queryset = get_object_or_404(Cat, id=cat_id)
            cat = self.serializer_class(queryset)
            return Response(cat.data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, cat_id):
        try:
            cat = get_object_or_404(Cat, id=cat_id)
            serializer = self.serializer_class(cat, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, cat_id):
        try:
            cat = get_object_or_404(Cat, id=cat_id)
            cat.delete()
            return Response({'success': True}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FeedingsIndex(APIView):
    serializer_class = FeedingSerializer

    def get(self, request, cat_id):
        try:
            queryset = Feeding.objects.filter(cat=cat_id)
            return Response(self.serializer_class(queryset, many=True).data, status=status.HTTP_200_OK)
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, cat_id):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            queryset = Feeding.objects.filter(cat=cat_id)
            feedings = FeedingSerializer(queryset, many=True)
            return Response(feedings.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PhotoDetail(APIView):
    serializer_class = PhotoSerializer

    def post(self, request, cat_id):
        try:
            # Set Cat ID for Photo
            data = request.data.copy()
            data["cat"] = int(cat_id)

            #  Find Existing Photo and Delete if exists
            existing_photo = Photo.objects.filter(cat=cat_id)
            if existing_photo:
                existing_photo.delete()

            # Create Serializer Instance and Validate
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                cat = get_object_or_404(Cat, id=cat_id)
                serializer.save()
                return Response(CatSerializer(cat).data, status=status.HTTP_200_OK)
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            print(str(err))
            return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ToyIndex(generics.ListCreateAPIView):
  serializer_class = ToySerializer
  queryset = Toy.objects.all()

class ToyDetail(APIView):
  serializer_class = ToySerializer
  lookup_field = 'id'
  
  def get(self, request, toy_id):
    try:
      toy = get_object_or_404(Toy, id=toy_id)
      return Response(self.serializer_class(toy).data, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  def put(self, request, toy_id):
    try:
      toy = get_object_or_404(Toy, id=toy_id)
      serializer = self.serializer_class(toy, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

  def delete(self, request, toy_id):
    try:
      toy = Toy.objects.get(id=toy_id)
      toy.delete()
      return Response({'success': True}, status=status.HTTP_200_OK)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)