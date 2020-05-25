
from django import forms

from .models import Garden



class GardenForm(forms.ModelForm):
    class Meta:
        model = Garden
        fields = ['name','id_user']

        # widgets = {'id_user': forms.Textarea() }

