from django import forms
from django.forms import ModelForm
from .models import Vehicle


class VehicleForm(ModelForm):
    name = forms.TextInput()

    class Meta:
        model = Vehicle
        fields = ['name', 'brand', 'model', 'reg_number', 'tech_insp', 'vehicle_image']

