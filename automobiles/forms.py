from django import forms
from django.forms import ModelForm
from .models import Vehicle


class VehicleForm(ModelForm):
    brand = forms.TextInput()
    class Meta:
        model = Vehicle
        fields = ['brand', 'model', 'reg_number']
