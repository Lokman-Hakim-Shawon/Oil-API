from .views import CategoryList, CategoryDetail
from django.urls import path

urlpatterns = [
    path("",CategoryList.as_view(), name='category-list'),
    path('<int:pk>/', CategoryDetail.as_view(),name='category-detail')
]