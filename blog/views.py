from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'Judul' : 'BLOGKU',
        'Pembuat' : 'Meh',
        'nav' : [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'ABOUT']
        ]
    }

    return render(request, 'blog/index.html', context)

def recent(request):
    return HttpResponse('<h1> Ini adalah recent post </h1>')