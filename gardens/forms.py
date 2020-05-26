from django import forms

from .models import Garden


class GardenForm(forms.ModelForm):
    id_user = forms.IntegerField(widget = forms.HiddenInput(),required=False)

    class Meta:
        model = Garden
        fields = ['name', 'id_user']

