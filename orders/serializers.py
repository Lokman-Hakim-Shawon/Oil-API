from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'
        read_only_fields=[
            "total_price",
            "status",
            "created_at",
        ]
    def create(self,validated_data):
        product = validated_data["product"]
        quantity=validated_data['quantity']
        
        if quantity>product.stock:
            raise serializers.ValidationError(
                {
                    "Quantity exceeds available stock."
                }
            )
        
        total_price=product.price * quantity
        
        product.stock -= quantity
        product.save()
        
        order=Order.objects.create(
            total_price=total_price,
            **validated_data
        )
        return order