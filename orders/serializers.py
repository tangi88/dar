from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        # fields = ('customer_name', 'comment', 'user')


class OrderProductSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=15, decimal_places=2)
    discount = serializers.DecimalField(max_digits=5, decimal_places=2)
    sum = serializers.DecimalField(max_digits=15, decimal_places=2)

