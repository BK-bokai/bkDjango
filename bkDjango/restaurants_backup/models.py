from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.name

class Comment(models.Model):
    visitor = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    email   = models.CharField(max_length=200)
    publish_date = models.DateTimeField()
    Restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=3, decimal_places=0)
    comment = models.CharField(max_length=50, blank=True)
    is_spicy = models.BooleanField(default=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    # 如果決定之後想讓資料都照某項特性排列，
    # 但卻不想每次這麼麻煩地打這些
    # 在Food類別中加入Meta
    # 記得更動Meta時也需做migration

    class Meta:
        ordering = ['price']  # 價格從小到大排

    # q.choice_set.all()
    # q.choice_set.create(choice_text='Not much', votes=0)
    # q.choice_set.count()
    # q.choice_set.filter(choice_text__startswith='Just hacking')
    # Restaurant.objects.get(id=1).food_set.filter(id=1).update(price=13)
    # Restaurant.objects.get(id=1).food_set.get(id=1).price



class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

    # A3=Author(name='李白')
    # A3.save()
    # B1 = Book(title = '唐詩三百首')
    # B1.save()
    # B1.authors.add(A3)
