from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ProductViewSet, OrderViewSet, OrderItemViewSet, StockMovementViewSet

# API için Router oluştur
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'stock-movements', StockMovementViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]





from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='inventory_home'),
]
