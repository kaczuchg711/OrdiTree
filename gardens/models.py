# coding=utf-8
from django.db import models

# Create your models here.
class Garden(models.Model):
    name = models.CharField(max_length=30)
    id_user = models.IntegerField(default=0) # Jak Jakub ogarnie uzytkowników: user models.ForeignKey(auth_user, on_delete=models.CASCADE)


###### przyklad z fk
    # from django.db import models
    #
    # class Reporter(models.Model):
    #     first_name = models.CharField(max_length=30)
    #     last_name = models.CharField(max_length=30)
    #     email = models.EmailField()
    #
    #     def __str__(self):
    #         return "%s %s" % (self.first_name, self.last_name)
    #
    # class Article(models.Model):
    #     headline = models.CharField(max_length=100)
    #     pub_date = models.DateField()
    #     reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    #
    #     def __str__(self):
    #         return self.headline
    #
    #     class Meta:
    #         ordering = ['headline']
