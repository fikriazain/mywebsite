from django.shortcuts import render

def index(request):
    context = {
        'Judul' : 'ABOUT',
        'Pembuat' : 'Fikri'
    }
    return render(request, 'about/index.html', context)

def cerita(request):
    context = {
        'Judul' : 'ABOUT Cerita',
        'Pembuat' : 'F Cerita'
    }
    return render(request, 'about/index.html', context)