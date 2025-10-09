from django.shortcuts import render, get_object_or_404 , redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Note, Reaction
from .forms import CommentForm, PhotoForm
from .models import Photo




def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def notes_index(request):
    notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': notes})


def note_detail(request, note_id):
    note = Note.objects.get(id=note_id)
    comment_form = CommentForm()
    photo_form = PhotoForm()
    return render(request, 'notes/detail.html', {
        'note': note,
        'comment_form': comment_form,
        'photo_form': photo_form
    })


def add_photo(request, note_id):
    form = PhotoForm(request.POST)
    if form.is_valid():
        new_photo = form.save(commit=False)
        new_photo.note_id = note_id
        existing = Photo.objects.filter(note_id=note_id).first()
        if existing:
            existing.delete()
        new_photo.save()
    return redirect('note_detail', note_id=note_id)

class NoteCreate(CreateView):
    model = Note
    fields = ['title', 'body']

    def get_success_url(self):
        return reverse('note_detail', kwargs={'note_id': self.object.id})


class NoteUpdate(UpdateView):
    model = Note
    fields = ['title', 'body']


class NoteDelete(DeleteView):
    model = Note
    success_url = '/notes/'


class ReactionList(ListView):
    model = Reaction


class ReactionDetail(DetailView):
    model = Reaction


class ReactionCreate(CreateView):
    model = Reaction
    fields = '__all__'


class ReactionUpdate(UpdateView):
    model = Reaction
    fields = ['emoji', 'color']  


class ReactionDelete(DeleteView):
    model = Reaction
    success_url = '/reactions/'
