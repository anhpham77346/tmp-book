from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Customer

# Form đăng ký
class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Tên đăng nhập", 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Email", 
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="Mật khẩu", 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="Xác nhận mật khẩu", 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Customer
        fields = ['username', 'email', 'password1', 'password2']


# Form đăng nhập
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Tên đăng nhập", 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Mật khẩu", 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

