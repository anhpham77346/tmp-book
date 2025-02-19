from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from customer.models import Customer
from order.models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from book.models import Book
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes

# Create your views here.
@permission_classes([IsAdminUser])
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

@permission_classes([IsAdminUser])
class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

@login_required(login_url='login')
def cart_view(request):
    # Giả sử user đã đăng nhập và có customer_id
    customer = get_object_or_404(Customer, username=request.user.username)
    
    # Lấy giỏ hàng của khách hàng
    cart, created = Cart.objects.get_or_create(customer=customer)
    
    # Lấy danh sách sản phẩm trong giỏ hàng
    cart_items = CartItem.objects.filter(cart=cart)

    # Tính tổng tiền
    total_price = sum(item.book.price * item.quantity for item in cart_items)

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

@login_required(login_url='login')
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart')

@login_required(login_url='login')
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    customer = get_object_or_404(Customer, username=request.user.username)

    # Kiểm tra xem giỏ hàng có tồn tại không, nếu không thì tạo mới
    cart, created = Cart.objects.get_or_create(customer=customer)

    # Kiểm tra xem sách đã có trong giỏ chưa
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)

    # Nếu sách đã có trong giỏ, tăng số lượng
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

@login_required(login_url='login')
def checkout_from_cart(request):
    cart = get_object_or_404(Cart, customer=request.user)

    if not cart.cartitem_set.exists():
        return redirect("cart")  # Nếu giỏ hàng trống, quay lại giỏ hàng

    total_price = sum(item.book.price * item.quantity for item in cart.cartitem_set.all())

    if request.method == "POST":
        # Khi người dùng xác nhận đơn hàng, mới tạo Order
        order = Order.objects.create(
            customer=request.user,
            total_price=total_price,
            status="pending"
        )

        # Chuyển các sản phẩm từ giỏ hàng vào đơn hàng
        for item in cart.cartitem_set.all():
            OrderItem.objects.create(
                order=order,
                book=item.book,
                quantity=item.quantity,
                price=item.book.price
            )

        # Xóa giỏ hàng sau khi tạo đơn hàng
        cart.cartitem_set.all().delete()

        return redirect("checkout")  # Chuyển sang trang thanh toán

    # Nếu là GET request, hiển thị trang xác nhận đặt hàng
    return render(request, "payment/checkout_confirmation.html", {"cart": cart, "total_price": total_price})

