from django.db import models

# Create your models here.
class Garden:
    name = "garden name"
    user = "no user"

    def __init__(self,name,user):
        self.name = name
        self.user = user