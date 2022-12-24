from django.shortcuts import render, get_object_or_404
from products.models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import generics
from cart.forms import CartAddProductForm


def product(request, product_id):
    prod = get_object_or_404(Product, id=product_id)
    cart_add_form = CartAddProductForm(initial={'quantity': 1})
    images = ProductImage.objects.filter(product=prod).order_by('-is_main')
    if not images.exists():
        images = None

    return render(request, 'products/product.html', {'product': prod,
                                                     'cart_add_form': cart_add_form,
                                                     'images': images})


class ProductAPIView(APIView):
    def get(self, request):
        p = Product.objects.all()
        return Response({'products': ProductSerializer(p, many=True).data})

    def post(self, request):
        products = request.data.get('products')
        if not products:
            return Response({'error': 'products is empty'})

        data = []
        for prod in products:
            id_1c = prod.get('id_1c')

            try:
                instance = Product.objects.get(id_1c=id_1c)
                serializer = ProductSerializer(data=prod, instance=instance)
            except:
                serializer = ProductSerializer(data=prod)

            if serializer.is_valid():
                serializer.save()

            data.append({'id_1c': id_1c, 'error': serializer.errors})

        return Response({'products': data})


class ProductCategoryAPIView(APIView):
    def post(self, request):
        categories = request.data.get('categories')
        if not categories:
            return Response({'error': 'categories is empty'})

        data = []
        for category in categories:
            id_1c = category.get('id_1c')

            try:
                instance = ProductCategory.objects.get(id_1c=id_1c)
                serializer = ProductCategorySerializer(data=category, instance=instance)
            except:
                serializer = ProductCategorySerializer(data=category)

            if serializer.is_valid():
                serializer.save()

            data.append({'id_1c': id_1c, 'error': serializer.errors})

        return Response({'categories': data})


class ProductUnitAPIView(APIView):
    def post(self, request):
        units = request.data.get('units')
        if not units:
            return Response({'error': 'units is empty'})

        data = []
        for unit in units:
            code = unit.get('code')

            try:
                instance = ProductUnit.objects.get(code=code)
                serializer = ProductUnitSerializer(data=unit, instance=instance)
            except:
                serializer = ProductUnitSerializer(data=unit)

            if serializer.is_valid():
                serializer.save()

            data.append({'code': code, 'error': serializer.errors})

        return Response({'units': data})


class ProductImageAPIView(APIView):
    def post(self, request):
        files = request.data.get('files')
        if not files:
            return Response({'error': 'files is empty'})

        data = []
        for file in files:
            id_1c = file.get('id_1c')

            try:
                instance = ProductImage.objects.get(id_1c=id_1c)
                serializer = ProductImageSerializer(data=file, instance=instance)
            except:
                serializer = ProductImageSerializer(data=file)

            if serializer.is_valid():
                serializer.save()

            data.append({'id_1c': id_1c, 'error': serializer.errors})

        return Response({'files': data})


# class ProductAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer



