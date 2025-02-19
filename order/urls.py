from django.urls import path
from .views import order_management

urlpatterns = [
    path('order-list/', order_management, name='order_management'),
]
