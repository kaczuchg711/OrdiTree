from django.db import models

# Create your models here.
class MessageOrdiTree(models.Model):
    sender = models.ForeignKey(User,related_name="sender")
    reciever = models.ForeignKey(User,related_name="reciever")
    message_content = models.CharField(max_length=300)
    created = models.DateTimeField()