from django.db import models
from products.models import Product
# Create your models here.
class Order(models.Model):
    STATUS_CHOICES=[
        ("Pending","Pending"),
        ("Confirmed","Confirmed"),
        ("Shipped","Shipped"),
        ("Delivered","Delivered"),
    ]
    customer_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    address=models.TextField()
    product=models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="orders"
    )
    quantity=models.PositiveIntegerField(default=1)
    total_price=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default="Pending")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.customer_name