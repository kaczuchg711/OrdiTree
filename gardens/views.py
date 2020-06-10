from django.forms import HiddenInput
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from gardens.forms import GardenForm

from gardens.models import Garden


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
    context = {
        "user_id": request.user.id
    }

    if request.method == 'POST':
        print(request.POST)
        print(request.POST['garden'])

        request.session['garden_name'] = request.POST['garden']
        print(request.session['garden_name'] )
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
