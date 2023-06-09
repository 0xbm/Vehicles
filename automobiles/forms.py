from django import forms
from django.forms import ModelForm
from .models import Vehicle


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['name', 'brand', 'model', 'reg_num', 'tech_insp', 'driver', 'vehicle_image', 'description']

        labels = {
            'name': '',
            'brand': '',
            'model': '',
            'reg_num': '',
            'tech_insp': '',
            'driver': '',
            'vehicle_image': '',
            'description': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vehicle Name'}),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vehicle Brand'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vehicle Model'}),
            'reg_num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Registry Number'}),
            'tech_insp': forms.DateInput(
                attrs={'class': 'form-control', 'placeholder': 'Technical Inspection Date (YYYY:MM:DD)'}),
            'driver': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Driver'}),
            # 'vehicle_image': forms.TextInput(attrs={'class': 'form-control','placeholder':'Vehicle Name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }
