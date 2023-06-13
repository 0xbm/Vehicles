from django.shortcuts import render, redirect
from .forms import VehicleForm, BrandForm, ModelForm, DriverForm
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
    time = now.strftime('%H:%M:%S')
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


def list_brand(request):
    brand_list = Brand.objects.all()
    return render(request, 'list_brand.html', {'brand_list': brand_list})


def show_brand(request, brand_id):
    brand_show = Brand.objects.get(pk=brand_id)
    return render(request, 'show_brand.html', {'brand_show': brand_show})


def update_brand(request, brand_id):
    brand_update = Brand.objects.get(pk=brand_id)
    form = BrandForm(request.POST or None, instance=brand_update)
    if form.is_valid():
        form.save()
        redirect('update_brand.html')

    context = {"form": form, 'brand_update': brand_update}
    return render(request, 'update_brand.html', context)


def add_brand(request):
    submitted = False
    if request.method == "POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = BrandForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {"form": form, 'submitted': submitted}
    return render(request, "add_brand.html", context)


def list_model(request):
    model_list = Model.objects.all()
    return render(request, 'list_model.html', {'model_list': model_list})


def show_model(request, model_id):
    model_show = Model.objects.get(pk=model_id)
    return render(request, 'show_model.html', {'model_show': model_show})


def update_model(request, model_id):
    model_update = Model.objects.get(pk=model_id)
    form = ModelForm(request.POST or None, instance=model_update)
    if form.is_valid():
        form.save()
        redirect('update_model.html')

    context = {"form": form, 'model_update': model_update}
    return render(request, 'update_model.html', context)


def add_model(request):
    submitted = False
    if request.method == "POST":
        form = ModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = ModelForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {"form": form, 'submitted': submitted}
    return render(request, "add_model.html", context)


def list_driver(request):
    driver_list = Driver.objects.all()
    return render(request, 'list_driver.html', {'driver_list': driver_list})


def show_driver(request, driver_id):
    driver_show = Driver.objects.get(pk=driver_id)
    return render(request, 'show_driver.html', {'driver_show': driver_show})


def update_driver(request, driver_id):
    driver_update = Model.objects.get(pk=driver_id)
    form = DriverForm(request.POST or None, instance=driver_update)
    if form.is_valid():
        form.save()
        redirect('update_driver.html')

    context = {"form": form, 'driver_update': driver_update}
    return render(request, 'update_driver.html', context)


def add_driver(request):
    submitted = False
    if request.method == "POST":
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = DriverForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {"form": form, 'submitted': submitted}
    return render(request, "add_driver.html", context)
