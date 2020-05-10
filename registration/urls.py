from django.urls import path

from . import views
from .views import Registration

urlpatterns=[
    path('', Registration, name='Registration'),
    path('',views.index, name='index'),
]