from django.urls import path

from . import views
from .views import LoginPage

urlpatterns=[
    path('', LoginPage, name='Login'),
    path('',views.index, name='index'),
]