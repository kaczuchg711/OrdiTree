from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# Create your views here.
def LoginPage(request):
    template = "LoginPage.html"
    context = {}
    return render(request,template,context)