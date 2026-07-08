from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from .serializers import ProductSerializer
from .models import Product
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.    
class ProductList(ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends=[SearchFilter,OrderingFilter,DjangoFilterBackend]
    search_fields=[
        'name',
        'price',
        'brand',
        'title',
        'category__name'
    ]
    ordering_fields=[
        'price',
        'name',
        'stock'
    ]
    
    filterset_fields=[
        'category',
        'brand',
        'price'
    ]
    
class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
