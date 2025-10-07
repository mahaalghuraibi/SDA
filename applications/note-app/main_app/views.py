from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Note

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def notes_index(request):
    notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': notes})

def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, 'notes/detail.html', {'note': note})

class NoteCreate(CreateView):
    model = Note
    fields = ['title', 'body']
    success_url = '/notes/'

    def get_success_url(self):
        return reverse('note_detail', kwargs={'note_id': self.object.id})

class NoteUpdate(UpdateView):
    model = Note
    fields = ['title', 'body']

class NoteDelete(DeleteView):
    model = Note
    success_url = '/notes/'
