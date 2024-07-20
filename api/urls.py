from django.urls import path
from .views import (
    CategoryCreateAPIView, CategoryDetailAPIView, CategoryUpdateAPIView, CategoryListAPIView,
    DishCreateAPIView, DishDetailAPIView, DishUpdateAPIView, DishListAPIView,
    ReviewCreateAPIView, ReviewDetailAPIView, ReviewUpdateAPIView, ReviewListAPIView,
    OrderCreateAPIView, OrderDetailAPIView, OrderUpdateAPIView, OrderListAPIView
)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('categories/<int:pk>/update/', CategoryUpdateAPIView.as_view(), name='category-update'),

    path('dishes/', DishListAPIView.as_view(), name='dish-list'),
    path('dishes/create/', DishCreateAPIView.as_view(), name='dish-create'),
    path('dishes/<int:pk>/', DishDetailAPIView.as_view(), name='dish-detail'),
    path('dishes/<int:pk>/update/', DishUpdateAPIView.as_view(), name='dish-update'),

    path('reviews/', ReviewListAPIView.as_view(), name='review-list'),
    path('reviews/create/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),
    path('reviews/<int:pk>/update/', ReviewUpdateAPIView.as_view(), name='review-update'),

    path('orders/', OrderListAPIView.as_view(), name='order-list'),
    path('orders/create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view(), name='order-detail'),
    path('orders/<int:pk>/update/', OrderUpdateAPIView.as_view(), name='order-update'),
]


