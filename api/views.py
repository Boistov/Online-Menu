from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters,permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Category, Dish, Review, Order, Feedback, CartItem
from .serializers import CategorySerializer, DishSerializer, ReviewSerializer, OrderSerializer, Feedback,FeedbackSerializer,CartItemSerializer, OrderSerializer




class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
  

class CategoryDeleteAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DishCreateAPIView(generics.CreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class DishDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class DishUpdateAPIView(generics.UpdateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class DishListAPIView(generics.ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['name']
    permission_classes = [permissions.IsAuthenticated]


class DishDeleteAPIView(generics.DestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewUpdateAPIView(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDeleteAPIView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderUpdateAPIView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['total_price']
    search_fields = ['user__username']
    permission_classes = [permissions.IsAuthenticated]

class OrderDeleteAPIView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class FeedbackCreateAPIView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FeedbackListAPIView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FeedbackDetailAPIView(generics.RetrieveAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FeedbackUpdateAPIView(generics.UpdateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FeedbackDeleteAPIView(generics.DestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class CartItemCreateAPIView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class CartItemListAPIView(generics.ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class CartItemDeleteAPIView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class CartOrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        cart_items = CartItem.objects.filter(user=request.user)
        if not cart_items.exists():
            return Response({'error': 'Cart is empty'}, status=400)

        order_data = {
            'user': request.user.id,
            'total_price': sum(item.dish.price * item.quantity for item in cart_items),
            'items': [{'dish': item.dish.id, 'quantity': item.quantity} for item in cart_items]
        }
        serializer = self.get_serializer(data=order_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        CartItem.objects.filter(user=request.user).delete()
        return Response(serializer.data, status=201)
    

