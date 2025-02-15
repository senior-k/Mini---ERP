"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # Yeni eklendi

# Ana sayfa için basit bir view
def home(request):
    return HttpResponse("<h1>Hoş geldiniz! Ana sayfa çalışıyor.</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),  # Inventory app'in URL'leri
    path('', home, name='home'),  # Ana sayfa yönlendirmesi
]
from django.contrib import admin
from django.urls import path, include
from .views import home  # Yeni ekledik!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
    path('', home, name='home'),  # Ana sayfa artık şablonla çalışacak!
]


