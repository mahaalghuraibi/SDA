from django.contrib import admin
from .models import Note, MoodCheck, Photo, Reaction

admin.site.register(Note)
admin.site.register(MoodCheck)
admin.site.register(Photo)
admin.site.register(Reaction)
