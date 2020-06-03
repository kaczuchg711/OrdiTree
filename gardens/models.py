# coding=utf-8
from django.db import models

# Create your models here.
class Garden(models.Model):
    name = models.CharField(max_length=30)
    id_user = models.IntegerField(default=300)

