from django.shortcuts import render, redirect
from .forms import ContactForm


# Create your views here.
def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            print("OK")
            return redirect("automobiles:index")
    else:
        form = ContactForm()

    context = {"form": form}
    return render(request, "contact/index.html", context)
