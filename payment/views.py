from django.shortcuts import render, redirect
from order.models import Order
from .models import Payment

def payment_page(request):
    order = Order.objects.filter(customer=request.user, status="pending").last()

    if not order:
        return redirect("home")

    return render(request, "payment/checkout.html", {"order": order})
