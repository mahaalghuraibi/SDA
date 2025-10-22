from rest_framework import serializers
from django import forms
from .models import Cat, Feeding, Photo, Toy

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = '__all__'


class ToySerializer(serializers.ModelSerializer):

    class Meta:
        model = Toy
        fields = '__all__'
        
class CatSerializer(serializers.ModelSerializer):
    # this will allow us to include the photo in the cat without having to query for it! Neat!
    photo = PhotoSerializer(read_only=True)
    toys = ToySerializer(many=True, read_only=True)

    class Meta:
        model = Cat
        fields = '__all__'

# new serializer below
class FeedingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeding
        fields = '__all__'








