from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes
from django.contrib.auth.decorators import user_passes_test
from .models import Book
from .forms import BookForm

# Kiểm tra user có phải admin không
def is_admin(user):
    return user.is_authenticated and user.is_staff  # Chỉ admin mới có quyền

@permission_classes([IsAdminUser])
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def home(request):
    # books = Book.objects.all().order_by('-created_at')[:10]  # Hiển thị 10 sách mới nhất
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def book_list(request):
    books = Book.objects.all()
    print(books)
    return render(request, 'book/book_list.html', {'books': books})

@user_passes_test(is_admin)
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'book/book_form.html', {'form': form})

@user_passes_test(is_admin)
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)
    return render(request, 'book/book_form.html', {'form': form})
