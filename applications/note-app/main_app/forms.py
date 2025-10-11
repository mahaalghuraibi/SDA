from django import forms
from .models import Comment, Photo
from .models import Reaction

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['url']

class ReactionForm(forms.ModelForm):
    class Meta:
        model = Reaction
        fields = ['emoji'] 

