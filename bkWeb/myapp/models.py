from django.db import models

# Create your models here.
class Store(models.Model):
    boss = models.CharField(max_length=20)
    store_name = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.store_name

class Food(models.Model):
    food_name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=3, decimal_places=0)
    food_store = models.ForeignKey(Store,on_delete=models.CASCADE)
    def __str__(self):
        return self.food_name