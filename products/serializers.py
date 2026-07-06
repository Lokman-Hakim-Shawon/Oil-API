from rest_framework import serializers
from  .models import Product
from categories.models import Category
class ProductSerializer(serializers.ModelSerializer):
    category=serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name')
    class Meta:
        model=Product
        fields='__all__'