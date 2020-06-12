from django import forms
from django.forms.utils import ErrorList

from .models import associative_Gardens



class associativePlantGardenForm(forms.ModelForm):
    class Meta:
        model = associative_Gardens
        fields = ['id_garden','id_plant']