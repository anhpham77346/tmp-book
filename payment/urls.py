from django.urls import path
from .views import payment_page

urlpatterns = [
    path('checkout/', payment_page, name='checkout'),
]
