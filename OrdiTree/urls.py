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

from gardens.views import show_gardens, show_panel, show_add_garden, add_Garden_to_db
from gardens.models import Garden

from plants.views import show_plants, add_plant_to_garden, delatePlant

from contact.views import contactPanel, delateMessage
from registration.views import register

from userPanel.views import userPanel ,changePassword

urlpatterns = [
    path('',auth_views.LoginView.as_view(redirect_authenticated_user=True),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('admin/', admin.site.urls),
    path('gardens/', show_gardens,name='gardens'),
    path('gardens/mainPanel', show_panel,name='mainPanel'),
    path('gardens/addGarden', show_add_garden,name='add garden'),
    path('gardens/addGardenSave', add_Garden_to_db,name='add garden to db'),
    path('userPanel/',userPanel,name='userPanel' ),
    path('userPanel/changePassword',changePassword,name='changePassword' ),
    path('plants/',show_plants,name='show_plants' ),
    path('plants/delatePlant', delatePlant,name='delatePlant'),
    path('contact/',contactPanel,name='contactPanel' ),
    path('contact/delateMessage',delateMessage,name='delateMessage'),
    path('plants/add_plant_to_garden',add_plant_to_garden,name='add_plant_to_garden'),
]
