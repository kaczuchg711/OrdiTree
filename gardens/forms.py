from django import forms

from .models import Garden


class GardenForm(forms.ModelForm):


    def __init__(self, id_user, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=None, empty_permitted=False, instance=None, use_required_attribute=None, renderer=None):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance,
                         use_required_attribute, renderer)

        self.id_user = forms.IntegerField(widget=forms.HiddenInput(), required=False, initial=id_user)


    class Meta:
        model = Garden
        fields = ['name', 'id_user']

