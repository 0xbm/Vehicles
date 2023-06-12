from django.shortcuts import render, redirect
from .forms import VehicleForm
from datetime import datetime
from .models import Brand, Model, Vehicle, Driver
from django.http import HttpResponseRedirect


# Create your views here.
# def index(request):
#     return HttpResponse("Hello, you are at the automobile index.")


def home(request):
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    context = {"current_year": current_year, 'time': time}
    return render(request, "home.html", context)


def add_vehicle(request):
    submitted = False
    if request.method == "POST":
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = VehicleForm()
        if 'submitted' in request.GET:
            submitted = True

    now = datetime.now()
    current_year = now.year
    time = now.strftime('%I:%M:%S %p')
    context = {"form": form, "current_year": current_year, 'time': time, 'submitted': submitted}
    return render(request, "add_vehicle.html", context)


def all_vehicles(request):
    vehicles_all = Vehicle.objects.all()
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    context = {'vehicles_all': vehicles_all, "current_year": current_year, 'time': time}
    return render(request, 'all_vehicles.html', context)


def list_vehicles(request):
    vehicles_list = Vehicle.objects.all()
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    context = {'vehicles_list': vehicles_list, "current_year": current_year, 'time': time}
    return render(request, 'list_vehicles.html', context)


def show_vehicle(request, vehicle_id):
    vehicle_show = Vehicle.objects.get(pk=vehicle_id)
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    context = {'vehicle_show': vehicle_show, "current_year": current_year, 'time': time}
    return render(request, 'show_vehicle.html', context)


def search_vehicles(request):
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    if request.method == 'POST':
        searched = request.POST['searched']
        vehicles = Vehicle.objects.filter(name__contains=searched)
        return render(request, 'search_vehicles.html',
                      {'searched': searched, 'vehicles': vehicles, "current_year": current_year, 'time': time})
    else:
        vehicles_search = Vehicle.objects.all()
        context = {'vehicles_search': vehicles_search, "current_year": current_year, 'time': time}
        return render(request, 'search_vehicles.html', context)


def update_vehicle(request, vehicle_id):
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    vehicle_update = Vehicle.objects.get(pk=vehicle_id)
    form = VehicleForm(request.POST or None, instance=vehicle_update)
    if form.is_valid():
        form.save()
        redirect('update_vehicle.html')

    context = {"form": form, 'vehicle_update': vehicle_update, "current_year": current_year, 'time': time}
    return render(request, 'update_vehicle.html', context)
