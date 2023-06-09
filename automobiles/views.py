from django.shortcuts import render, redirect
from .forms import VehicleForm
from datetime import datetime
from .models import Brand, Model, Vehicle
from django.http import HttpResponseRedirect


# Create your views here.
# def index(request):
#     return HttpResponse("Hello, you are at the automobile index.")


def home(request):
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%I:%M:%S %p')
    context = {"current_year": current_year, 'time': time}
    return render(request, "home.html", context)


def add_vehicle(request):
    submitted = False
    if request.method == "POST":
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
        # return redirect('automobiles:add_vehicle')
    else:
        form = VehicleForm()
        if 'submitted' in request.GET:
            submitted = True

    now = datetime.now()
    current_year = now.year
    time = now.strftime('%I:%M:%S %p')
    context = {"form": form, "current_year": current_year, 'time': time, 'submitted': submitted}
    return render(request, "add_vehicle.html", context)


def list_vehicles(request):
    vehicle_list = Vehicle.objects.all()
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%I:%M:%S %p')
    context = {'vehicle_list': vehicle_list, "current_year": current_year, 'time': time}
    return render(request, 'list_vehicles.html', context)
