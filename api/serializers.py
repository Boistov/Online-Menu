from rest_framework import serializers
from .models import Category, Dish, Review, Order, Feedback, CartItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'

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
        fields = '__all__'

    def get_items(self, obj):
        items = CartItem.objects.filter(order=obj)
        return CartItemSerializer(items, many=True).data

class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Feedback
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    dish = DishSerializer(read_only=True)
    
    class Meta:
        model = CartItem
        fields = '__all__'
