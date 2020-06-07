from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class changeUserData(ModelForm):

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')
    def save(self, commit=True):
        user = super(changeUserData, self).save(commit)
    def is_valid(self):
        return super().is_valid()