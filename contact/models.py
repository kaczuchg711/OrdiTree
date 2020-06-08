from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MessageOrdiTree(models.Model):
    sender = models.ForeignKey(User,related_name="sender",on_delete=models.CASCADE,)
    reciever = models.ForeignKey(User,related_name="receiver",on_delete=models.CASCADE)
    message_content = models.CharField(max_length=300)
    created = models.DateTimeField(default=0)