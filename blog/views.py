from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'blog/index.html')

def recent(request):
    return HttpResponse('<h1> Ini adalah recent post </h1>')