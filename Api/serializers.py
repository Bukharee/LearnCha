from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Product
from Users.serializers import PublicUserSerializer


class ProductSerializer(serializers.ModelSerializer):
    user = PublicUserSerializer(read_only=True)
    discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "user",
            "title",
            "content",
            "price",
            "discount",
        ]

    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.sale_price
