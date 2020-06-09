from django.shortcuts import render

# Create your views here.

def show_plants(request, *args, **kwargs):
    return render(request, "plants/plants.html")