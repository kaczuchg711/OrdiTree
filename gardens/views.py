from django.forms import HiddenInput
from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
from datetime import date
from datetime import datetime
from plants.models import Plant
from gardens.forms import GardenForm
from gardens.models import Garden
from plants.models import associative_Gardens


def show_gardens(request, *args, **kwargs):
    gardenss = Garden.objects.filter(id_user=request.user.id)
    context = {
        "title": "gardens",
        "gardens_names": [g.name for g in gardenss]
    }
    if request.user.id is None:
        return render(request, "registration/nonePermission.html", context)

    return render(request, "gardens/choice.html", context)


def show_panel(request, *args, **kwargs):
    if request.method == 'POST':
        garden_name = request.POST['garden']
        print("\n\n\n\n\n tak \n\n\n\n")
        request.session['garden_name'] = garden_name
        garden = Garden.objects.filter(id_user=request.user.id, name=garden_name)[0]
    else:
        garden = Garden.objects.filter(id_user=request.user.id, name=request.session['garden_name'])[0]

    PlantsMain = associative_Gardens.objects.filter(id_garden=garden.id)
    ListOfCommunicats = []
    today = date.today()
    for i in PlantsMain:
        tempPlant = Plant.objects.filter(id=i.id_plant_id)[0]
        if (today - i.last_manuring_date).days > tempPlant.manuring_frequency_byDays:
            ListOfCommunicats.append(
                [tempPlant.name, i.id, (today - i.last_manuring_date).days, "Potrzebuje nawożenia"])
        if (today - i.last_watering_date).days > tempPlant.watering_frequency_byDays:
            ListOfCommunicats.append([tempPlant.name, i.id, (today - i.last_watering_date).days, "Potrzebuje podlania"])
        if (today - i.last_cutting_date).days > tempPlant.cutting_frequency_byDays:
            ListOfCommunicats.append([tempPlant.name, i.id, (today - i.last_cutting_date).days, "Potrzebuje obcięcia"])

    context = {
        "user_id": request.user.id,
        # "currentPlants":PlantsMain,
        "PlantsWarnings": ListOfCommunicats
    }

    if request.method == 'POST':
        request.session['garden_name'] = request.POST['garden']

    if not context.get("user_id", False):
        return render(request, "registration/nonePermission.html", context)


    return render(request, "gardens/mainPanel.html", context)


def show_add_garden(request):
    if request.method == 'POST':

        form = GardenForm(request.POST or None)

        if form.is_valid():
            form.save()

        context = {
            'form': form
        }

        return render(request, "gardens/addGarden.html", context)


# i only add this fun because i dont know how add default hide input for user id
def add_Garden_to_db(request):
    gardens = Garden.objects.all().filter(id_user=request.user.id)
    gardensnames = []

    for i in gardens:
        gardensnames.append(i.name)

    gareden = Garden()

    gareden.name = request.POST["name"]
    if gareden.name in gardensnames:

        form = GardenForm(request.POST or None)

        context = {
            'form': form,
            'warning': 'this name is in use'
        }
        return render(request, "gardens/addGarden.html", context)
    else:
        gareden.id_user = request.user.id
        gareden.save()
        return redirect('gardens')
