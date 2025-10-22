from rest_framework import serializers
from .models import Note, MoodCheck, Photo, Reaction

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

    class Meta:
        model = Note
        fields = '__all__'


class MoodCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodCheck
        fields = '__all__'
