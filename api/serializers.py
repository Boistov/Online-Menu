from rest_framework import serializers
from .models import Category, Dish, Review, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' 

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__' 

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__' 

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__' 
