from django.shortcuts import render
from products.models import Product, ProductImage


def index_page(request):
    products = Product.objects.filter()
    products_images = ProductImage.objects.filter(is_main=True)
    return render(request, 'indexpage/index.html', locals())

