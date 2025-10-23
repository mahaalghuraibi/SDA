from rest_framework import serializers
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
    photo = PhotoSerializer(read_only=True)
    toys = ToySerializer(many=True, read_only=True)

    class Meta:
        model = Cat
        fields = '__all__'


class FeedingSerializer(serializers.ModelSerializer):
    meal_display = serializers.CharField(source='get_meal_display', read_only=True)

    class Meta:
        model = Feeding
        fields = '__all__' 









