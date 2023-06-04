from django.shortcuts import render, redirect
from .forms import VehicleForm
from datetime import datetime
from .models import Brand, Model, Vehicle

from django.http import HttpResponse


# Create your views here.
# def index(request):
#     return HttpResponse("Hello, you are at the automobile index.")


def home(request):
    now = datetime.now()
    current_year = now.year
    return render(request, "home.html", {"current_year": current_year})


def add_vehicle(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('automobiles:add_vehicle')
    else:
        form = VehicleForm()

    context = {"form": form}
    return render(request, "add_vehicle.html", context)


def list_vehicles(request):
    vehicle_list = Vehicle.objects.all()
    return render(request, 'list_vehicles.html', {'vehicle_list': vehicle_list})
