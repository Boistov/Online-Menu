from django.contrib import admin
from .models import Review, Order, Dish, Category


admin.site.register(Review)
admin.site.register(Order)
admin.site.register(Dish)
admin.site.register(Category)
