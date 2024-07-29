from django.urls import path
from .views import (
    CategoryCreateAPIView,CategoryDetailAPIView,CategoryUpdateAPIView,CategoryListAPIView,CategoryDeleteAPIView,
    DishCreateAPIView,DishDetailAPIView,DishUpdateAPIView,DishListCreateAPIView,DishDeleteAPIView,ReviewCreateAPIView,
    ReviewDetailAPIView,ReviewUpdateAPIView,ReviewListAPIView,ReviewDeleteAPIView,OrderCreateAPIView,OrderDetailAPIView,
    OrderUpdateAPIView,OrderListCreateAPIView,OrderDeleteAPIView,FeedbackCreateAPIView,FeedbackListAPIView,FeedbackDetailAPIView,
    FeedbackUpdateAPIView,FeedbackDeleteAPIView,CartItemCreateAPIView,CartItemListAPIView,CartItemDeleteAPIView,CartOrderCreateAPIView,
)

urlpatterns = [
    path('categories/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('categories/<int:pk>/update/', CategoryUpdateAPIView.as_view(), name='category-update'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/delete/', CategoryDeleteAPIView.as_view(), name='category-delete'),
    
    path('dishes/create/', DishCreateAPIView.as_view(), name='dish-create'),
    path('dishes/<int:pk>/', DishDetailAPIView.as_view(), name='dish-detail'),
    path('dishes/<int:pk>/update/', DishUpdateAPIView.as_view(), name='dish-update'),
    path('dishes/', DishListCreateAPIView.as_view(), name='dish-list'),
    path('dishes/<int:pk>/delete/', DishDeleteAPIView.as_view(), name='dish-delete'),
    
    path('reviews/create/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),
    path('reviews/<int:pk>/update/', ReviewUpdateAPIView.as_view(), name='review-update'),
    path('reviews/', ReviewListAPIView.as_view(), name='review-list'),
    path('reviews/<int:pk>/delete/', ReviewDeleteAPIView.as_view(), name='review-delete'),
    
    path('orders/create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view(), name='order-detail'),
    path('orders/<int:pk>/update/', OrderUpdateAPIView.as_view(), name='order-update'),
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list'),
    path('orders/<int:pk>/delete/', OrderDeleteAPIView.as_view(), name='order-delete'),
    
    path('feedbacks/create/', FeedbackCreateAPIView.as_view(), name='feedback-create'),
    path('feedbacks/', FeedbackListAPIView.as_view(), name='feedback-list'),
    path('feedbacks/<int:pk>/', FeedbackDetailAPIView.as_view(), name='feedback-detail'),
    path('feedbacks/<int:pk>/update/', FeedbackUpdateAPIView.as_view(), name='feedback-update'),
    path('feedbacks/<int:pk>/delete/', FeedbackDeleteAPIView.as_view(), name='feedback-delete'),
    
    path('cartitems/create/', CartItemCreateAPIView.as_view(), name='cartitem-create'),
    path('cartitems/', CartItemListAPIView.as_view(), name='cartitem-list'),
    path('cartitems/<int:pk>/delete/', CartItemDeleteAPIView.as_view(), name='cartitem-delete'),
    
    path('cartorder/create/', CartOrderCreateAPIView.as_view(), name='cartorder-create'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]