from django.contrib import admin
from .models import Restaurant,Food,Author,Book

# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'address')
    search_fields = ('name',)

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'comment', 'is_spicy', 'restaurant')
    list_filter = ('is_spicy',)
    # ordering = ('-price')


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food, FoodAdmin)
