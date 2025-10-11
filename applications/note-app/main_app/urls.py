from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('notes/', views.notes_index, name='notes_index'),               
    path('notes/<int:note_id>/', views.note_detail, name='note_detail'),  
    path('notes/create/', views.NoteCreate.as_view(), name='note_create'), 
    path('notes/<int:pk>/update/', views.NoteUpdate.as_view(), name='note_update'), 
    path('notes/<int:pk>/delete/', views.NoteDelete.as_view(), name='note_delete'), 
    path('reactions/create/', views.ReactionCreate.as_view(), name='reaction-create'),
    path('reactions/<int:pk>/', views.ReactionDetail.as_view(), name='reaction-detail'),
    path('reactions/', views.ReactionList.as_view(), name='reaction-index'),
    path('reactions/<int:pk>/update/', views.ReactionUpdate.as_view(), name='reaction-update'),
    path('reactions/<int:pk>/delete/', views.ReactionDelete.as_view(), name='reaction-delete'),
    path('<int:note_id>/add-photo/', views.add_photo, name='add_photo'),
    path('notes/<int:note_id>/reactions/create/', views.add_reaction, name='add_reaction'),
    path('accounts/signup/', views.signup, name='signup'),

]
