from django.shortcuts import render
from  rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Payment
from .serializers import PaymentSerializer
# Create your views here.

class PaymentList(ListCreateAPIView):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
    
class PaymentDetail(RetrieveUpdateDestroyAPIView):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer