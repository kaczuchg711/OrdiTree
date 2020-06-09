from datetime import date

from django.db import models
# Create your models here.
from gardens.models import Garden


class Plant(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    temperature = models.IntegerField(default=20)
    last_manuring_date = models.DateField(default="2000-11-11")
    manuring_frequency_byDays = models.IntegerField(default=15)
    last_watering_date = models.DateField(default="2000-11-11")
    watering_frequency_byDays = models.IntegerField(default=3)
    last_cutting_date = models.DateField(default="2000-11-11")
    cutting_frequency_byDays = models.IntegerField(default=3)
    # this create MM table separate from Plant
    Garden = models.ManyToManyField(Garden)
