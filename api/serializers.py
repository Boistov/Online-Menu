from rest_framework import serializers
from .models import Category, Dish, Review, Order, Feedback, CartItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id', 'name', 'description', 'price', 'category', 'image']

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Review
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price', 'items', 'created_at']

    def get_items(self, obj):
        items = CartItem.objects.filter(order=obj)
        return CartItemSerializer(items, many=True).data

class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Feedback
        fields = ['id', 'user', 'message', 'created_at']

class CartItemSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    dish = DishSerializer(read_only=True)
    
    class Meta:
        model = CartItem
        fields = ['id', 'user', 'dish', 'quantity', 'created_at']
