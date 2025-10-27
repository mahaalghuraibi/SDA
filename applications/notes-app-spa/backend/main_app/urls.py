from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('notes/', views.NotesIndex.as_view(), name='note-index'),
    path('notes/<int:note_id>/', views.NoteDetail.as_view(), name='note-detail'),
    path('notes/<int:note_id>/moodchecks/', views.MoodChecksIndex.as_view(), name='moodcheck-create'),
    path('notes/<int:note_id>/photo/', views.PhotoDetail.as_view(), name='photo-detail'),

    path('reactions/', views.ReactionIndex.as_view(), name='reaction-index'),
    path('reactions/<int:reaction_id>/', views.ReactionDetail.as_view(), name='reaction-detail'),

    path('notes/<int:note_id>/add-reaction/<int:reaction_id>/', views.AddReactionToNote.as_view(), name='add-reaction-to-note'),
    path('notes/<int:note_id>/remove-reaction/<int:reaction_id>/', views.RemoveReactionFromNote.as_view(), name='remove-reaction-from-note'),

    path('users/signup/', views.CreateUserView.as_view(), name='signup'),
    path('users/login/', views.LoginView.as_view(), name='login'),
    path('users/verify/', views.VerifyUserView.as_view(), name='verify'),

]
