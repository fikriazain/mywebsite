from django.http import HttpResponse

#  method view
def homepage(request):
    return  HttpResponse('<h1> halo dunia </h1>')


def about(request):
    return HttpResponse('<h1> Ini about </h1>')