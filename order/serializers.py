from product.serializers import ProductSerializer
from .models import Order
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Nested product details

    class Meta:
        model = Order
        fields = '__all__'
