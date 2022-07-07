from rest_framework import serializers


class ProductInlineSerializer(serializers.Serializer):
    title = serializers.CharField()


class PublicUserSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    other_products = serializers.SerializerMethodField(read_only=True)

    def get_other_products(self, obj):
        user = obj
        my_products = user.product_set.all()
        return ProductInlineSerializer(my_products, many=True).data
