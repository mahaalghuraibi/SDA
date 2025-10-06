from django.shortcuts import render
from django.http import HttpResponse
from .models import Cat
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cat_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})


def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})

class CatCreate(CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']
    success_url = '/cats/'

    def get_success_url(self):
        return reverse('cat_detail', kwargs={'cat_id': self.object.id})

class CatUpdate(UpdateView):
    model = Cat
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'