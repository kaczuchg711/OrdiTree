from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('.\registration\index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def Registration(request):
    template = "Registration.html"
    context = {}
    return render(request,template,context)