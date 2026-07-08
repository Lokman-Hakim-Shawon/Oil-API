from .views import OrderList,OderDetail
from django.urls import path

urlpatterns=[
    path('',OrderList.as_view(),name='order-list'),
    path('<int:pk>/',OderDetail.as_view(),name='order-detail')
]