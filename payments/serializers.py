from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__'
        read_only_fields=[
            "payment_status",
            "transaction_id",
            "paid_amount",
            "created_at",
        ]
    def create(self,validated_data):
        order=validated_data["order"]
        
        payment = Payment.objects.create(
            paid_amount=order.total_price,
            **validated_data
        )
        
        return payment