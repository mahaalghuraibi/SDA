from django import forms
from .models import Comment, Photo

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['url']



