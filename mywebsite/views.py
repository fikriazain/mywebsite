from django.shortcuts import render

def index(request):
    context = {
        'Judul' : 'WEBSITE OFFICIAL',
        'Pembuat' : 'Fikri Aufaa Zain',
        'nav' : [
            ['/','Home'],
            ['/blog', 'Blog'],
            ['/about', 'About']
        ]
    }
    return render(request, 'index.html', context)
