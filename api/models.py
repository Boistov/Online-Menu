from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='dishes/')
    video = models.FileField(upload_to='videos/')
    kalories = models.DecimalField(max_digits=6, decimal_places=2)
    fat = models.DecimalField(max_digits=6, decimal_places=2)
    protein = models.DecimalField(max_digits=6, decimal_places=2)
    carbs = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Review(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username}'

class Order(models.Model):
    user = models.CharField(max_length=100)
    dishes = models.ManyToManyField(Dish)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order by {self.user}'



class Feedback(models.Model):
    message = models.TextField()

    def __str__(self):
        return self.message[:50]
    
class CartItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='cart_items')  # Add this field
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.dish.name} by {self.user.username}"
    
