from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# def index(request):
#     return HttpResponse("Hello, you are at the automobile index.")

def index(request):
    return render(request, "index.html")

# todo dodaj css do widoku
# todo przezuc style z index.html do css
# todo dodaj btn obok edit (+) albo u gory
