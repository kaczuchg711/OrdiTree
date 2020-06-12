from django.shortcuts import render

# Create your views here.
from plants.models import Plant
from plants.models import associative_Gardens


def show_plants(request, *args, **kwargs):

    # how to get this 29 ?
    ids_plants = associative_Gardens.objects.filter(id_garden=29)

    print("przed for")
    for i in ids_plants:
        print(i.id_plant.id)

    print("po for")
    plants_obj = Plant.objects.all()

    a = []

    for i in ids_plants:
        a.append(Plant.objects.filter(id=i.id_plant.id)[0])



    #  musze przypisac tym id u gory obiekty Plants


    context = {
        'user_plants' : a
    }

    return render(request, "plants/plants.html", context)