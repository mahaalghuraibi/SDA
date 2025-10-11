from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note_detail', kwargs={'note_id': self.id})

class Comment(models.Model):
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.ForeignKey('Note', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment on {self.note.title}"

        
class Reaction(models.Model):
    emoji = models.CharField(max_length=5)
    color = models.CharField(max_length=20)
    note = models.ForeignKey('Note', related_name='reactions', on_delete=models.CASCADE)

    def __str__(self):
        return self.emoji

    def get_absolute_url(self):
        return reverse('reaction-detail', kwargs={'pk': self.id})


class Photo(models.Model):
    url = models.CharField(max_length=250)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    note = models.OneToOneField('Note', on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for note_id: {self.note.id} @{self.url}"
