import os
import django
from django.conf import settings

# Ayar dosyasını belirt
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Django uygulamasını başlat
django.setup()

# Şimdi sınıfı oluştur
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)



import os
from django.conf import settings

# Ayar dosyasını belirt
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Django ayarlarını başlat
settings.configure()


from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model) :
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('pending', 'Beklemede'),
        ('shipped', 'Kargolandı'),
        ('delivered', 'Teslim Edildi'),
        ('canceled', 'İptal Edildi'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='pending')

    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class StockMovement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    movement_type_choices = [
        ('in', 'Giriş'),
        ('out', 'Çıkış'),
    ]
    movement_type = models.CharField(max_length=10, choices=movement_type_choices)
    quantity = models.PositiveIntegerField()                
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.movement_type} - {self.quantity}"
