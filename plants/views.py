from django.shortcuts import render

# Create your views here.
from plants.models import Plant

def show_plants(request, *args, **kwargs):

    # how to get this 29 ?
    plants = Plant.objects.filter(Garden=29)

    context = {
        'user_plants' : plants
    }

    return render(request, "plants/plants.html", context)