from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from .serializers import ProductSerializer
from .models import Product
# Create your views here.    
class ProductList(ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
