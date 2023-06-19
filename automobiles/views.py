from django.shortcuts import render, redirect
from .forms import VehicleForm, BrandForm, ModelForm, DriverForm
from datetime import datetime
from .models import Brand, Model, Vehicle, Driver
from django.http import HttpResponseRedirect, HttpResponse

# CSV import
import csv

# PDF imports
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Pagination imports
from django.core.paginator import Paginator


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
    context = {"form": form, "current_year": current_year, 'time': time,
               'submitted': submitted}
    return render(request, "add_vehicle.html", context)


def all_vehicles(request):
    vehicles_all = Vehicle.objects.all().order_by('name')
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')

    context = {'vehicles_all': vehicles_all, "current_year": current_year,
               'time': time}
    return render(request, 'all_vehicles.html', context)


def list_vehicles(request):
    vehicles_list = Vehicle.objects.all()
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')

    # Set up Pagination
    p = Paginator(Vehicle.objects.all(), 2)
    page = request.GET.get('page')
    vehicles = p.get_page(page)
    nums = '-' * vehicles.paginator.num_pages

    context = {'vehicles_list': vehicles_list, "current_year": current_year,
               'time': time, 'vehicles': vehicles,
               'nums': nums}
    return render(request, 'list_vehicles.html', context)


def show_vehicle(request, vehicle_id):
    vehicle_show = Vehicle.objects.get(pk=vehicle_id)
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')

    context = {'vehicle_show': vehicle_show, "current_year": current_year,
               'time': time}
    return render(request, 'show_vehicle.html', context)


def search_vehicles(request):
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    if request.method == 'POST':
        searched = request.POST['searched']
        vehicles = Vehicle.objects.filter(name__contains=searched)
        return render(request, 'search_vehicles.html',
                      {'searched': searched, 'vehicles': vehicles,
                       "current_year": current_year, 'time': time})
    else:
        vehicles_search = Vehicle.objects.all()
        context = {'vehicles_search': vehicles_search,
                   "current_year": current_year, 'time': time}
        return render(request, 'search_vehicles.html', context)


def update_vehicle(request, vehicle_id):
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    vehicle_update = Vehicle.objects.get(pk=vehicle_id)
    form = VehicleForm(request.POST or None, request.FILES or None,
                       instance=vehicle_update)
    if form.is_valid():
        form.save()
        redirect('update_vehicle.html')

    context = {"form": form, 'vehicle_update': vehicle_update,
               "current_year": current_year, 'time': time}
    return render(request, 'update_vehicle.html', context)


def list_brand(request):
    brand_list = Brand.objects.all()
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    p = Paginator(Brand.objects.all(), 2)
    page = request.GET.get('page')
    brands = p.get_page(page)
    nums = '-' * brands.paginator.num_pages

    context = {'brand_list': brand_list, "current_year": current_year,
               'time': time, 'brands': brands,
               'nums': nums}
    return render(request, 'list_brand.html', context)


def show_brand(request, brand_id):
    brand_show = Brand.objects.get(pk=brand_id)
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    context = {'brand_show': brand_show, "current_year": current_year,
               'time': time}
    return render(request, 'show_brand.html', context)


def update_brand(request, brand_id):
    brand_update = Brand.objects.get(pk=brand_id)
    form = BrandForm(request.POST or None, instance=brand_update)
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    if form.is_valid():
        form.save()
        redirect('update_brand.html')

    context = {"form": form, 'brand_update': brand_update,
               "current_year": current_year, 'time': time}
    return render(request, 'update_brand.html', context)


def add_brand(request):
    submitted = False
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    if request.method == "POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = BrandForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {"form": form, 'submitted': submitted,
               "current_year": current_year, 'time': time}
    return render(request, "add_brand.html", context)


def list_model(request):
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    model_list = Model.objects.all()
    p = Paginator(Model.objects.all(), 2)
    page = request.GET.get('page')
    models = p.get_page(page)
    nums = '-' * models.paginator.num_pages
    context = {'model_list': model_list, "current_year": current_year,
               'time': time, 'models': models,
               'nums': nums}
    return render(request, 'list_model.html', context)


def show_model(request, model_id):
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    model_show = Model.objects.get(pk=model_id)
    context = {'model_show': model_show, "current_year": current_year,
               'time': time}
    return render(request, 'show_model.html', context)


def update_model(request, model_id):
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    model_update = Model.objects.get(pk=model_id)
    form = ModelForm(request.POST or None, instance=model_update)
    if form.is_valid():
        form.save()
        redirect('update_model.html')

    context = {"form": form, 'model_update': model_update,
               "current_year": current_year, 'time': time}
    return render(request, 'update_model.html', context)


def add_model(request):
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
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

    context = {"form": form, 'submitted': submitted,
               "current_year": current_year, 'time': time}
    return render(request, "add_model.html", context)


def list_driver(request):
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    driver_list = Driver.objects.all()
    p = Paginator(Driver.objects.all(), 2)
    page = request.GET.get('page')
    drivers = p.get_page(page)
    nums = '-' * drivers.paginator.num_pages
    context = {'driver_list': driver_list, "current_year": current_year,
               'time': time,'drivers': drivers,
               'nums': nums}
    return render(request, 'list_driver.html', context)


def show_driver(request, driver_id):
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    driver_show = Driver.objects.get(pk=driver_id)
    context = {'driver_show': driver_show, "current_year": current_year,
               'time': time}
    return render(request, 'show_driver.html', context)


def update_driver(request, driver_id):
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    driver_update = Driver.objects.get(pk=driver_id)
    form = DriverForm(request.POST or None, instance=driver_update)
    if form.is_valid():
        form.save()
        redirect('update_driver.html')

    context = {"form": form, 'driver_update': driver_update,
               "current_year": current_year, 'time': time}
    return render(request, 'update_driver.html', context)


def add_driver(request):
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
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

    context = {"form": form, 'submitted': submitted,
               "current_year": current_year, 'time': time}
    return render(request, "add_driver.html", context)


def delete_vehicle(request, vehicle_id):
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    vehicle_delete = Vehicle.objects.get(pk=vehicle_id)
    vehicle_delete.delete()
    context = {"current_year": current_year, 'time': time}
    return render(request, "home.html", context)


def delete_brand(request, brand_id):
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    brand_delete = Brand.objects.get(pk=brand_id)
    brand_delete.delete()
    context = {"current_year": current_year, 'time': time}
    return render(request, "home.html", context)


def delete_model(request, model_id):
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    model_delete = Model.objects.get(pk=model_id)
    model_delete.delete()
    context = {"current_year": current_year, 'time': time}
    return render(request, "home.html", context)


def delete_driver(request, driver_id):
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    driver_delete = Driver.objects.get(pk=driver_id)
    driver_delete.delete()
    context = {"current_year": current_year, 'time': time}
    return render(request, "home.html", context)


def vehicle_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=vehicles.txt'
    vehicles = Vehicle.objects.all()

    lines = []
    for vehicle in vehicles:
        lines.append(
            f'{vehicle.name}\n{vehicle.brand}\n{vehicle.model}\n{vehicle.reg_num}\n{vehicle.tech_inspection}\n{vehicle.vin_num}\n{vehicle.driver}\n\n\n')
    response.writelines(lines)
    return response


def vehicle_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=vehicles.csv'
    writer = csv.writer(response)
    vehicles = Vehicle.objects.all()
    writer.writerow(['Vehicle Name', 'Brand', 'Model', 'Registry Number',
                     'Technical Inspection', 'Vin', 'Driver'])

    for vehicle in vehicles:
        writer.writerow(
            [vehicle.name, vehicle.brand, vehicle.model, vehicle.reg_num,
             vehicle.tech_inspection, vehicle.vin_num,
             vehicle.driver])
    return response


def vehicle_pdf(request):
    # Create Bytestream buffer
    buffer = io.BytesIO()
    # Create canvas
    c = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
    # Create text object
    textobject = c.beginText()
    textobject.setTextOrigin(inch, inch)
    textobject.setFont("Helvetica", 14)

    vehicles = Vehicle.objects.all()
    lines = []

    for vehicle in vehicles:
        lines.append(vehicle.name)
        lines.append(str(vehicle.brand))
        lines.append(str(vehicle.model))
        lines.append(vehicle.reg_num)
        lines.append(str(vehicle.tech_inspection))
        lines.append(vehicle.vin_num)
        lines.append("============")

    for line in lines:
        textobject.textLine(line)

    c.drawText(textobject)
    c.showPage()
    c.save()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename='vehicle.pdf')
