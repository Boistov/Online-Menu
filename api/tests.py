from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category, Dish, Review, Order

class CategoryTests(APITestCase):
    def setUp(self):
        self.category_data = {'name': 'Test Category', 'description': 'Test description'}
        self.category = Category.objects.create(**self.category_data)

    def test_create_category(self):
        url = reverse('category-list-create')
        response = self.client.post(url, self.category_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_categories(self):
        url = reverse('category-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Category.objects.count())

    def test_get_category(self):
        url = reverse('category-detail', args=[self.category.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.category.name)

    def test_update_category(self):
        url = reverse('category-detail', args=[self.category.id])
        updated_data = {'name': 'Updated Category', 'description': 'Updated description'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, updated_data['name'])

    def test_delete_category(self):
        url = reverse('category-detail', args=[self.category.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Category.objects.filter(id=self.category.id).exists())


class DishTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', description='Test description')
        self.dish_data = {'name': 'Test Dish', 'description': 'Test description', 'category': self.category.id, 'price': 10.0}
        self.dish = Dish.objects.create(name='Test Dish', description='Test description', category=self.category, price=10.0)

    def test_create_dish(self):
        url = reverse('dish-list-create')
        response = self.client.post(url, self.dish_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_dishes(self):
        url = reverse('dish-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Dish.objects.count())

    def test_get_dish(self):
        url = reverse('dish-detail', args=[self.dish.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.dish.name)

    def test_update_dish(self):
        url = reverse('dish-detail', args=[self.dish.id])
        updated_data = {'name': 'Updated Dish', 'description': 'Updated description', 'category': self.category.id, 'price': 15.0}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.dish.refresh_from_db()
        self.assertEqual(self.dish.name, updated_data['name'])

    def test_delete_dish(self):
        url = reverse('dish-detail', args=[self.dish.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Dish.objects.filter(id=self.dish.id).exists())


class ReviewTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', description='Test description')
        self.dish = Dish.objects.create(name='Test Dish', description='Test description', category=self.category, price=10.0)
        self.review_data = {'dish': self.dish.id, 'rating': 5, 'comment': 'Great!'}
        self.review = Review.objects.create(dish=self.dish, rating=5, comment='Great!')

    def test_create_review(self):
        url = reverse('review-list-create')
        response = self.client.post(url, self.review_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_reviews(self):
        url = reverse('review-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Review.objects.count())

    def test_get_review(self):
        url = reverse('review-detail', args=[self.review.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['comment'], self.review.comment)

    def test_update_review(self):
        url = reverse('review-detail', args=[self.review.id])
        updated_data = {'dish': self.dish.id, 'rating': 4, 'comment': 'Good!'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.review.refresh_from_db()
        self.assertEqual(self.review.comment, updated_data['comment'])

    def test_delete_review(self):
        url = reverse('review-detail', args=[self.review.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Review.objects.filter(id=self.review.id).exists())


class OrderTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', description='Test description')
        self.dish = Dish.objects.create(name='Test Dish', description='Test description', category=self.category, price=10.0)
        self.order_data = {'dish': self.dish.id, 'quantity': 2, 'total_price': 20.0, 'status': 'Pending'}
        self.order = Order.objects.create(dish=self.dish, quantity=2, total_price=20.0, status='Pending')

    def test_create_order(self):
        url = reverse('order-list-create')
        response = self.client.post(url, self.order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_orders(self):
        url = reverse('order-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Order.objects.count())

    def test_get_order(self):
        url = reverse('order-detail', args=[self.order.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], self.order.status)

    def test_update_order(self):
        url = reverse('order-detail', args=[self.order.id])
        updated_data = {'dish': self.dish.id, 'quantity': 3, 'total_price': 30.0, 'status': 'Completed'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, updated_data['status'])

    def test_delete_order(self):
        url = reverse('order-detail', args=[self.order.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Order.objects.filter(id=self.order.id).exists())



