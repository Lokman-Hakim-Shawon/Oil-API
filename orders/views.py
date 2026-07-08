from django.shortcuts import render
from .serializers import OrderSerializer
from .models import Order
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
# Create your views here.
class OrderList(ListCreateAPIView):
      queryset=Order.objects.all()
      serializer_class=OrderSerializer
class OderDetail(RetrieveUpdateDestroyAPIView):
      queryset=Order.objects.all()
      serializer_class=OrderSerializer      
