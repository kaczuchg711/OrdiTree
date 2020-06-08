from django import forms
from django.forms.utils import ErrorList
from .models import MessageOrdiTree


class MessageOrdiTreeForm(forms.Form):
    sender = forms.CharField(max_length=100)
    reciever = forms.CharField(max_length=100)
    message_content = forms.CharField(widget=forms.Textarea)
    created = models.DateTimeField()
