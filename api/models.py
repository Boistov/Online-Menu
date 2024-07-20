from django.db import models

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

    def __str__(self):
        return self.name

class Review(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user}'

class Order(models.Model):
    user = models.CharField(max_length=100)
    dishes = models.ManyToManyField(Dish)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order by {self.user}'
