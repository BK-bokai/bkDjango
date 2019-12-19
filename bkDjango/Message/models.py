from django.db import models
from Users.models import User

# Create your models here.
class Messages(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    body    = models.TextField()
    reply_num = models.PositiveIntegerField(default = 0)
    create_at = models.DateTimeField()
    update_at = models.DateTimeField(null=True) 

    # def __str__(self):
    #     return self.food_name


# class Message_reply(models.Model):

class Replies(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Message = models.ForeignKey(Messages, on_delete=models.CASCADE)
    body    = models.TextField()
    create_at = models.DateTimeField()
    update_at = models.DateTimeField(null=True) 
