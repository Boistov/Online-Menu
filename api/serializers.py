from rest_framework import serializers
from .models import Category, Dish, Review, Order,Feedback, CartItem

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


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'message']



class CartItemSerializer(serializers.ModelSerializer):
    dish = DishSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'dish', 'quantity']

