from django.http import HttpResponse

def home(request):
    return HttpResponse("Inventory Ana Sayfa")






from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets
from .models import Customer, Product, Order, OrderItem, StockMovement
from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer, OrderItemSerializer, StockMovementSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class StockMovementViewSet(viewsets.ModelViewSet):
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer

    


