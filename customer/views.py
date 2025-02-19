from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm, LoginForm
from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes

@permission_classes([IsAdminUser])
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Đăng ký
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Đăng nhập sau khi đăng ký thành công
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'customer/register.html', {'form': form})

# Đăng nhập
def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'customer/login.html', {'form': form})

# Đăng xuất
def logout_view(request):
    logout(request)
    return redirect('home')
