from django.urls import path
from .views import Home, NotesIndex

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('notes/', NotesIndex.as_view(), name='note-index'),
]
