from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import VehicleForm


# Create your views here.
# def index(request):
#     return HttpResponse("Hello, you are at the automobile index.")


def index(request):
    return render(request, "index.html")


def vehicle(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('automobiles:vehicle')
    else:
        form = VehicleForm()

    context = {"form": form}
    return render(request, "add_vehicle.html", context)
