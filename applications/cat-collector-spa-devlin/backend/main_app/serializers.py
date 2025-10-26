from rest_framework import serializers
from .models import Cat, Feeding, Photo, Toy
from django.contrib.auth.models import User

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
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    photo = PhotoSerializer(read_only=True)
    toys = ToySerializer(many=True, read_only=True)
    
    class Meta:
        model = Cat
        fields = '__all__'

class FeedingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeding
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    # Add a password field, make it write-only
    # prevents allowing 'read' capabilities (returning the password via api response)
    password = serializers.CharField(write_only=True)  

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']  
        )
      
        return user


