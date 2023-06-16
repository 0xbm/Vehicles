from django import forms
from django.forms import ModelForm
from .models import Vehicle, Brand, Model, Driver


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['name', 'brand', 'model', 'reg_num', 'vin_num', 'tech_inspection', 'driver',
                  'description', 'vehicle_image']
        labels = {
            'name': '',
            'Brand': 'Brand',
            'model': 'Model',
            'reg_num': '',
            'vin_num': '',
            'tech_inspection': '',
            'driver': 'Driver/s',
            'description': '',
            'vehicle_image': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vehicle Name'}),
            'brand': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Vehicle Brand'}),
            'model': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Vehicle Model'}),
            'reg_num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Registry Number'}),
            'vin_num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'VIN'}),
            'tech_inspection': forms.DateInput(
                attrs={'class': 'form-control', 'placeholder': 'Technical Inspection Date (YYYY:MM:DD)'}),
            'driver': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Driver'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }


class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ['name']
        labels = {
            'name': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brand Name'}),
        }


class ModelForm(ModelForm):
    class Meta:
        model = Model
        fields = ['name']
        labels = {
            'name': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Model Name'}),
        }


class DriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = ['first_name', 'last_name']
        labels = {
            'first_name': '',
            'last_name': '',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
        }
