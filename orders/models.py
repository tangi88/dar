from django.db import models
from products.models import Product
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=48)
    customer_address = models.CharField(max_length=500, blank=True, null=True, default=None)
    comment = models.TextField(blank=True, null=True, default=None)
    sum = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    status = models.CharField(max_length=25, blank=True, null=True, default=None)

    def __str__(self):
        return 'Order %s' % self.pk

    # def save(
    #     self, force_insert=False, force_update=False, using=None, update_fields=None
    # ):
    #     super(Order, self).save()


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
    amount = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    sum = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.sum = self.amount * self.price

        super(OrderProduct, self).save()


def OrderProduct_post_save(sender, instance, created, **kwargs):
    all_products = OrderProduct.objects.filter(order=instance.order)
    total_sum = 0
    for item in all_products:
        total_sum += item.sum

    instance.order.sum = total_sum
    instance.order.save(force_update=True)


post_save.connect(OrderProduct_post_save, sender=OrderProduct)

