from django.shortcuts import render, redirect

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

    base_plants = Plant.objects.all()
    base_plants_names = [i.name for i in base_plants]

    context = {
        'user_plants': plants,
        'base_plants': base_plants_names
    }

    return render(request, "plants/plants.html", context)


def add_plant_to_garden(request, *args, **kwargs):
    if request.method == 'POST':
        apg = associative_Gardens()
        print("\n\n\n\n\n\n\n")
        print(request.POST['plant'])
        print("\n\n\n\n\n\n\n")
        # bierze tylko tuja a nie tuja szmaragd

        apg.id_plant = Plant.objects.filter(name=request.POST['plant'])[0]
        apg.id_garden = Garden.objects.filter(name=request.session['garden_name'], id_user=request.user.id)[0]
        apg.save()

    return redirect('show_plants')
