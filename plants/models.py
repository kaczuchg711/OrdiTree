from django.db import models
# Create your models here.
from gardens.models import Garden


class Plant(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    # this create MM table separate from Plant
    Garden = models.ManyToManyField(Garden)
