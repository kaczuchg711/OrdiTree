from django.shortcuts import render

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

    if not context.get("user_id",False):
        return render(request, "registration/nonePermission.html", context)

    return render(request, "gardens/mainPanel.html", context)


def show_add_garden(request):
    form = GardenForm(request.user.id,request.POST or None)
    form.fields['id_user'].widget.attrs['readonly'] = True
    form.fields['id_user'].widget.attrs['visible'] = False
    print(request.user.id)


    if form.is_valid():
        form.save()

    context = {
            'form': form
        }
    return render(request, "gardens/addGarden.html",context)
