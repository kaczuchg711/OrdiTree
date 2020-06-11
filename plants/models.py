from datetime import date

from django.db import models
# Create your models here.
from gardens.models import Garden


class Plant(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    temperature = models.IntegerField(default=20)
    manuring_frequency_byDays = models.IntegerField(default=15)
    watering_frequency_byDays = models.IntegerField(default=3)
    cutting_frequency_byDays = models.IntegerField(default=3)


class associative_Gardens(models.Model):
    id_garden = models.ForeignKey(Garden, on_delete=models.SET(0))
    id_plant = models.ForeignKey(Plant, on_delete=models.SET(0))
    last_cutting_date = models.DateField(default="2000-11-11")
    last_watering_date = models.DateField(default="2000-11-11")
    last_manuring_date = models.DateField(default="2000-11-11")
