from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    id_1c = models.CharField(max_length=100, blank=True, null=True, default=None)

    def __str__(self):
        return self.name


class ProductUnit(models.Model):
    code = models.CharField(max_length=25, blank=True, null=True, default=None)
    name = models.CharField(max_length=25, blank=True, null=True, default=None)
    description = models.CharField(max_length=100, blank=True, null=True, default=None)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default=None)
    article = models.CharField(max_length=25, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    category = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
    unit = models.ForeignKey(ProductUnit, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    leftover = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    id_1c = models.CharField(max_length=100, blank=True, null=True, default=None)
    code = models.CharField(max_length=11, blank=True, null=True, default=None)
    is_deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
    name = models.CharField(max_length=150, blank=True, null=True, default=None)
    is_main = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products_images/')
    id_1c = models.CharField(max_length=100, blank=True, null=True, default=None)

