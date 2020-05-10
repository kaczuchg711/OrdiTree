from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from gardens.models import Garden


def show_gardens(request, *args, **kwargs):
    gardenss = Garden.objects.filter(id_user = 0)
    print()
    print(gardenss[0].name)
    print()
    context = {
        "title": "gardens",
        "gardens_names": [g.name for g in gardenss]
    }
    return render(request, "gardens.html", context)
