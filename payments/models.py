from django.db import models
from orders.models import Order
# Create your models here.

class Payment(models.Model):
    PAYMENT_METHODS = [
        ("COD", "Cash on Delivery"),
        ("BKASH", "Bkash"),
        ("NAGAD", "Nagad"),
        ("ROCKET", "Rocket"),
        ("CARD", "Card Payment"),
    ]
    PAYMENT_STATUS=[
        ("PENDING","Pending"),
        ("COMPLETED","Completed"),
        ("FAILED","Failed"),
    ]
    
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name="payment"
    )
    payment_method=models.CharField(max_length=10,choices=PAYMENT_METHODS,default="COD")
    payment_status=models.CharField(max_length=10,choices=PAYMENT_STATUS,default="Pending")
    transaction_id=models.CharField(max_length=100, blank=True,null=True)
    paid_amount=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True,default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"payment #{self.id}"