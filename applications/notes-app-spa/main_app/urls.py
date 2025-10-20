from django.urls import path
from .views import NotesIndex, NoteDetail, MoodChecksIndex, Home , PhotoDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('notes/', NotesIndex.as_view(), name='note-index'),
    path('notes/<int:note_id>/', NoteDetail.as_view(), name='note-detail'),
    path('notes/<int:note_id>/moodchecks/', MoodChecksIndex.as_view(), name='moodcheck-create'),
    path('notes/<int:note_id>/photo/', PhotoDetail.as_view(), name='photo-detail'),

]
