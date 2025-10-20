from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('notes/', views.NotesIndex.as_view(), name='note-index'),
    path('notes/<int:note_id>/', views.NoteDetail.as_view(), name='note-detail'),
]
