from django.db import models
from django.urls import reverse

class Note(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note_detail', kwargs={'note_id': self.id})
