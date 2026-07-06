from django.db import models
from categories.models import Category
# Create your models here.
class Product(models.Model):
    category=models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    name=models.CharField(max_length=100,unique=True)
    title=models.CharField(max_length=200,blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField(default=0)
    brand=models.CharField(max_length=100,blank=True,null=True)
    weight=models.CharField(max_length=60)
    image=models.ImageField(upload_to='products/',blank=True,null=True)
    def __str__(self):
        return self.name