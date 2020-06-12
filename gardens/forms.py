from django import forms
from django.forms.utils import ErrorList

from .models import Garden


class GardenForm(forms.ModelForm):
    class Meta:
        model = Garden
        fields = ['name']

