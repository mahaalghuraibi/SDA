from rest_framework import serializers
from .models import Note, MoodCheck, Photo, Reaction
from django.contrib.auth.models import User  

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(read_only=True)
    reactions = ReactionSerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Note
        fields = '__all__'



class MoodCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodCheck
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
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
