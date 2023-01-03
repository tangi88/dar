from rest_framework import serializers
from .models import *


class ProductUnitSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25)
    code = serializers.CharField(max_length=25)
    description = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return ProductUnit.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data.get('code', instance.code)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        return instance


class ProductCategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    id_1c = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return ProductCategory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.id_1c = validated_data.get('id_1c', instance.id_1c)
        instance.save()

        return instance


def find_unit(unit_data):
    unit_code = unit_data.get('code', '')

    try:
        unit = ProductUnit.objects.get(code=unit_code)
    except:
        unit = None

    return unit


def find_category(category_data):
    category_id_1c = category_data.get('id_1c', '')

    try:
        category = ProductCategory.objects.get(id_1c=category_id_1c)
    except:
        category = None

    return category


def find_product(product_data):
    product_id_1c = product_data.get('id_1c', '')

    try:
        product_obj = Product.objects.get(id_1c=product_id_1c)
    except:
        product_obj = None

    return product_obj


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    article = serializers.CharField(max_length=25, allow_blank=True)
    code = serializers.CharField(max_length=11)
    description = serializers.CharField(max_length=500, allow_blank=True)
    is_deleted = serializers.BooleanField()
    id_1c = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=15, decimal_places=2)
    leftover = serializers.DecimalField(max_digits=15, decimal_places=3)
    unit = ProductUnitSerializer()
    category = ProductCategorySerializer()

    def create(self, validated_data):
        unit_data = validated_data.pop('unit')
        category_data = validated_data.pop('category')

        instance = Product.objects.create(**validated_data)
        instance.category = find_category(category_data)
        instance.unit = find_unit(unit_data)
        instance.save()

        return instance

    def update(self, instance, validated_data):
        unit_data = validated_data.pop('unit')
        category_data = validated_data.pop('category')

        instance.name = validated_data.get('name', instance.name)
        instance.article = validated_data.get('article', instance.article)
        instance.description = validated_data.get('description', instance.description)
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
        instance.id_1c = validated_data.get('id_1c', instance.id_1c)
        instance.code = validated_data.get('code', instance.code)
        instance.price = validated_data.get('price', instance.price)
        instance.leftover = validated_data.get('leftover', instance.leftover)

        instance.category = find_category(category_data)
        instance.unit = find_unit(unit_data)

        instance.save()

        return instance


class Base64Image(serializers.ImageField):

    def to_internal_value(self, data):
        import base64
        import uuid
        from django.core.files.base import ContentFile

        if 'data' in data and ';base64, ' in data:
            header, data = data.split(';base64, ')

        try:
            decoded_file = base64.b64decode(data)
        except:
            self.fail('invalid_image')

        file_name = str(uuid.uuid4())[:12]
        file_extension = self.get_file_extension(file_name, decoded_file)

        complete_file_name = "%s.%s" % (file_name, file_extension, )

        data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64Image, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)

        return extension


class ProductImageSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    is_main = serializers.BooleanField()
    product = ProductSerializer()
    image = Base64Image()
    id_1c = serializers.CharField(max_length=100)

    def create(self, validated_data):
        product_data = validated_data.pop('product')

        instance = ProductImage.objects.create(**validated_data)
        instance.product = find_product(product_data)
        instance.save()

        return instance

    def update(self, instance, validated_data):
        product_data = validated_data.pop('product')

        instance.name = validated_data.get('name', instance.name)
        instance.is_main = validated_data.get('is_main', instance.is_main)
        instance.product = find_product(product_data)
        instance.image = validated_data.get('image', instance.image)
        instance.id_1c = validated_data.get('id_1c', instance.id_1c)
        instance.save()

        return instance

