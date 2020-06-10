from django.shortcuts import render

# Create your views here.
from gardens.models import Garden

from plants.models import Plant
from plants.models import associative_Gardens


def show_plants(request, *args, **kwargs):

    garden_name = request.session['garden_name']

    garden = Garden.objects.filter(id_user=request.user.id, name=garden_name)[0]

    ids_plants = associative_Gardens.objects.filter(id_garden=garden.id)

    plants = []
    for i in ids_plants:
        plants.append(Plant.objects.filter(id=i.id_plant.id)[0])

    context = {
        'user_plants': plants
    }

    return render(request, "plants/plants.html", context)
