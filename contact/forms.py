from django import forms
from django.forms.utils import ErrorList
from .models import MessageOrdiTree


class MessageOrdiTreeForm(forms.ModelForm):

    class Meta:
        model = MessageOrdiTree
        fields = ('reciever','message_content',)

class MessageOrdiTreeFromDelate(forms.ModelForm):

    class Meta:
        model = MessageOrdiTree
        fields = ('id',)