from .models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    business = serializers.StringRelatedField()  # Display business name

    class Meta:
        model = Product
        fields = '__all__'
