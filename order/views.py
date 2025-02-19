from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order

@login_required(login_url='login')
def order_management(request):
    if not request.user.is_staff:
        return redirect('home')

    orders = Order.objects.all()

    if request.method == "POST":
        order_id = request.POST.get("order_id")
        new_status = request.POST.get("status")
        order = get_object_or_404(Order, id=order_id)
        order.status = new_status
        order.save()
        return redirect("order_management")

    return render(request, "order/order_management.html", {"orders": orders})
