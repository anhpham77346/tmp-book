from django.urls import path
from .views import cart_view, remove_from_cart, add_to_cart, checkout_from_cart

urlpatterns = [
    path('', cart_view, name='cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('add/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path("checkout-from-cart/", checkout_from_cart, name="checkout_from_cart"),
]
