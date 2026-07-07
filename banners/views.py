from django.shortcuts import render
from .models import Banner
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from .serializers import BannerSerializer
# Create your views here.
class BannerList(ListCreateAPIView):
    queryset=Banner.objects.all()
    serializer_class=BannerSerializer
    
class BannerDetail(RetrieveUpdateDestroyAPIView):
    queryset=Banner.objects.all()
    serializer_class=BannerSerializer
