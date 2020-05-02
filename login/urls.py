from django.urls import path
from .views import LoginPage

urlpatterns=[
    path('',LoginPage, name='Login'),
]