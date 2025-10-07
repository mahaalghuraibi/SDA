from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('notes/', views.notes_index, name='notes_index'),               
    path('notes/<int:note_id>/', views.note_detail, name='note_detail'),  
    path('notes/create/', views.NoteCreate.as_view(), name='note_create'), 
    path('notes/<int:pk>/update/', views.NoteUpdate.as_view(), name='note_update'), 
    path('notes/<int:pk>/delete/', views.NoteDelete.as_view(), name='note_delete'), 
]
