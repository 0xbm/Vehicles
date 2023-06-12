from django import forms
from django.forms import ModelForm
from .models import Vehicle


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['name', 'brand', 'model', 'reg_num', 'vin_num', 'tech_inspection', 'driver', 'vehicle_image',
                  'description']
        labels = {
            'name': '',
            'brand': 'Brand',
            'model': 'Model',
            'reg_num': '',
            'vin_num': '',
            'tech_inspection': '',
            'driver': '',
            'vehicle_image': '',
            'description': '',
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
            'vehicle_image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vehicle Image'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }
