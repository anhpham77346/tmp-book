from django.db import models

class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Đang chờ xác nhận'),
        ('confirmed', 'Đã xác nhận'),
        ('rejected', 'Bị từ chối')
    ]
    order = models.OneToOneField("order.Order", on_delete=models.CASCADE)
    bank_account = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Payment {self.transaction_id} for Order {self.order.id}"
