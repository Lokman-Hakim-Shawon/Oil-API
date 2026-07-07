from django.urls import path
from .views import BannerList, BannerDetail
urlpatterns=[
    path("",BannerList.as_view(), name='banner-list'),
    path('<int:pk>/', BannerDetail.as_view(),name='banner-detail')
]