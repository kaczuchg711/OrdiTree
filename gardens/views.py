from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def show_gardens(request, *args, **kwargs):
    context = {
        "title": "gardens",
        "gardens": ["garden1", "garden2", "garden3"]
    }
    return render(request, "gardens.html", context)
