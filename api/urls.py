from django.urls import path
from .views import (
    CategoryListAPIView, CategoryCreateAPIView, CategoryDetailAPIView, CategoryUpdateAPIView, CategoryDeleteAPIView,
    DishListAPIView, DishCreateAPIView, DishDetailAPIView, DishUpdateAPIView, DishDeleteAPIView,
    ReviewListAPIView, ReviewCreateAPIView, ReviewDetailAPIView, ReviewUpdateAPIView, ReviewDeleteAPIView,
    OrderListAPIView, OrderCreateAPIView, OrderDetailAPIView, OrderUpdateAPIView, OrderDeleteAPIView,
    FeedbackCreateAPIView, FeedbackListAPIView, FeedbackDetailAPIView, FeedbackUpdateAPIView, FeedbackDeleteAPIView,
    CartItemCreateAPIView, CartItemListAPIView, CartItemDeleteAPIView, CartOrderCreateAPIView
)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('categories/<int:pk>/detail', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('categories/<int:pk>/update/', CategoryUpdateAPIView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteAPIView.as_view(), name='category-delete'),

    path('dishes/', DishListAPIView.as_view(), name='dish-list'),
    path('dishes/create/', DishCreateAPIView.as_view(), name='dish-create'),
    path('dishes/<int:pk>/detail', DishDetailAPIView.as_view(), name='dish-detail'),
    path('dishes/<int:pk>/update/', DishUpdateAPIView.as_view(), name='dish-update'),
    path('dishes/<int:pk>/delete/', DishDeleteAPIView.as_view(), name='dish-delete'),

    path('reviews/', ReviewListAPIView.as_view(), name='review-list'),
    path('reviews/create/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('reviews/<int:pk>/detail', ReviewDetailAPIView.as_view(), name='review-detail'),
    path('reviews/<int:pk>/update/', ReviewUpdateAPIView.as_view(), name='review-update'),
    path('reviews/<int:pk>/delete/', ReviewDeleteAPIView.as_view(), name='review-delete'),

    path('orders/', OrderListAPIView.as_view(), name='order-list'),
    path('orders/create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('orders/<int:pk>/detail', OrderDetailAPIView.as_view(), name='order-detail'),
    path('orders/<int:pk>/update/', OrderUpdateAPIView.as_view(), name='order-update'),
    path('orders/<int:pk>/delete/', OrderDeleteAPIView.as_view(), name='order-delete'),

    path('feedback/', FeedbackListAPIView.as_view(), name='feedback-list'),
    path('feedback/create/', FeedbackCreateAPIView.as_view(), name='feedback-create'),
    path('feedback/<int:pk>/', FeedbackDetailAPIView.as_view(), name='feedback-detail'),
    path('feedback/<int:pk>/update/', FeedbackUpdateAPIView.as_view(), name='feedback-update'),
    path('feedback/<int:pk>/delete/', FeedbackDeleteAPIView.as_view(), name='feedback-delete'),
    
    path('cart/', CartItemListAPIView.as_view(), name='cart-list'),
    path('cart/add/', CartItemCreateAPIView.as_view(), name='cart-add'),
    path('cart/<int:pk>/delete/', CartItemDeleteAPIView.as_view(), name='cart-delete'),
    path('cart/order/', CartOrderCreateAPIView.as_view(), name='cart-order'),
]