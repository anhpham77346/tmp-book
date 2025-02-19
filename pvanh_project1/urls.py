"""
URL configuration for pvanh_project1 project.

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

from rest_framework.routers import DefaultRouter
from customer.views import CustomerViewSet
from cart.views import CartViewSet, CartItemViewSet
from book.views import BookViewSet, book_list

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'carts', CartViewSet, basename='cart')
router.register(r'cart-items', CartItemViewSet, basename='cartitem')
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', book_list, name="home"),
    path('customer/', include('customer.urls')),
    path('book/', include('book.urls')),
    path('cart/', include('cart.urls')),
    path('payment/', include('payment.urls')),
    path('order/', include('order.urls')),
]
