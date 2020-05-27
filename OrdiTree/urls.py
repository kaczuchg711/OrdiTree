"""OrdiTree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from gardens.views import show_gardens
from gardens.views import show_panel
from gardens.views import show_add_garden
from gardens.views import add_Garden_to_db

from gardens.models import Garden
from registration.views import register
from registration.views import register

urlpatterns = [
    path('',auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('admin/', admin.site.urls),
    path('gardens/', show_gardens,name='gardens'),
    path('gardens/mainPanel', show_panel,name='mainPanel'),
    path('gardens/addGarden', show_add_garden,name='add garden'),
    path('gardens/addGardenSave', add_Garden_to_db,name='add garden to db'),

]
