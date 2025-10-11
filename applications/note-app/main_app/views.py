from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Note, Reaction, Photo
from .forms import CommentForm, PhotoForm, ReactionForm



# ---------- Auth Views ----------

class Home(LoginView):
    template_name = 'home.html'


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('notes_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)



# ---------- Static Page ----------

def about(request):
    return render(request, 'about.html')



# ---------- Notes (Function Views) ----------


@login_required
def notes_index(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/index.html', {'notes': notes})


@login_required
def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    like_count = note.reactions.filter(emoji='like').count()
    love_count = note.reactions.filter(emoji='love').count()
    laugh_count = note.reactions.filter(emoji='laugh').count()

    photo_form = PhotoForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.note_id = note_id
            comment.save()
            return redirect('note_detail', note_id=note_id)
    else:
        comment_form = CommentForm()

    return render(request, 'notes/detail.html', {
        'note': note,
        'comment_form': comment_form,
        'photo_form': photo_form,
        'like_count': like_count,
        'love_count': love_count,
        'laugh_count': laugh_count,
    })


@login_required
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


@login_required
def add_reaction(request, note_id):
    form = ReactionForm(request.POST)
    if form.is_valid():
        new_reaction = form.save(commit=False)
        new_reaction.note_id = note_id
        existing = Reaction.objects.filter(note_id=note_id).first()
        if existing:
            existing.delete()
        new_reaction.save()
    return redirect('note_detail', note_id=note_id)



# ---------- Notes (Class Views) ----------


class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'body']

    def get_success_url(self):
        return reverse('note_detail', kwargs={'note_id': self.object.id})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'body']


class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = '/notes/'



# ---------- Reactions ----------

class ReactionList(LoginRequiredMixin, ListView):
    model = Reaction


class ReactionDetail(LoginRequiredMixin, DetailView):
    model = Reaction


class ReactionCreate(LoginRequiredMixin, CreateView):
    model = Reaction
    fields = '__all__'


class ReactionUpdate(LoginRequiredMixin, UpdateView):
    model = Reaction
    fields = ['emoji', 'color']


class ReactionDelete(LoginRequiredMixin, DeleteView):
    model = Reaction
    success_url = '/reactions/'
