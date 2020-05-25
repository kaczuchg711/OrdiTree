from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from gardens.models import Garden


def show_gardens(request, *args, **kwargs):
    gardenss = Garden.objects.filter(id_user = 0)
    context = {
        "title": "gardens",
        "gardens_names": [g.name for g in gardenss]
    }
    return render(request, "gardens/choice.html", context)

def show_panel(request, *args, **kwargs):
    gardenss = Garden.objects.filter(id_user = 0)
    context = {
        "user_id" : request.user.id
    }
    return render(request, "gardens/mainPanel.html",context)




