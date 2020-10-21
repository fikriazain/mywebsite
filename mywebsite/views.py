from django.shortcuts import render

def index(request):
    context = {
        'Judul' : 'WEBSITE OFFICIAL',
        'Pembuat' : 'Fikri Aufaa Zain'
    }
    return render(request, 'index.html', context)
