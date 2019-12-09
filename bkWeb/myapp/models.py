from django.db import models
from django.http import HttpResponse, Http404, HttpResponseRedirect


# Create your models here.
class Store(models.Model):
    boss = models.CharField(max_length=20)
    store_name = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.store_name

    def get_absolute_url(self):
        return HttpResponseRedirect(reverse('myapp:UpdateStoreForm', args=(self.id)))


class Food(models.Model):
    food_name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=3, decimal_places=0)
    food_store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.food_name

class Comment(models.Model):
    visitor = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    email   = models.CharField(max_length=200)
    publish_date = models.DateTimeField()
    Store = models.ForeignKey(Store,on_delete=models.CASCADE)
    def __str__(self):
        return self.visitor
