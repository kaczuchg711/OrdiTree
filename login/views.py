from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


# Create your views here.
def index(request):
    template = loader.get_template('.\login\index.html')
    context = {}
    return HttpResponse(template.render(context, request))


# Create your views here.
def LoginPage(request):
    template = "LoginPage.html"
    context = {}
    return render(request