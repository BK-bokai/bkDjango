from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    fullName = models.CharField(max_length=128,verbose_name="全名")
    website = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.fullName + ' (' + self.username + ')'

