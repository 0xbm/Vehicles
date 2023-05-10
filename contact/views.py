from django.shortcuts import render, redirect
from .forms import ContactForm


# Create your views here.
def index(request):
    form = ContactForm(request.POST)

    context = {"form": form}
    return render(request, "contact/index.html", context)
