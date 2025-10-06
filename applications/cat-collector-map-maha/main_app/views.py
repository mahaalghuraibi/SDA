from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    print("Hey you hit the home route!!!")
    return HttpResponse("<h1>Hello Maha </h1>")
def about(request):
    return render(request, 'about.html') 