from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from .models import Category
from .serializers import CategorySerializer
# Create your views here.
class CategoryList(ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    
class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer