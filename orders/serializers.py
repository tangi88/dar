from rest_framework import serializers
from .models import Order


# class OrderSerializer(serializers.Serializer):
#     user_id = serializers.IntegerField()
#     # user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
#     customer_email = serializers.CharField(max_length=100)
#     customer_name = serializers.CharField(max_length=100)
#     customer_phone = serializers.CharField(max_length=48)
#     customer_address = serializers.CharField(max_length=500)
#     comment = serializers.CharField()
#     sum = serializers.DecimalField(max_digits=15, decimal_places=2)
#     created = serializers.DateTimeField(read_only=True)
#     updated = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data):
#         return Order.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.updated = validated_data.get('updated', instance.updated)
#         instance.save()
#         return instance

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        # fields = ('customer_name', 'comment', 'user')

