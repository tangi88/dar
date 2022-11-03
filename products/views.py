from django.shortcuts import render
from products.models import Product


def product(request, product_id):
    product = Product.objects.get(id=product_id)

    session_key = request.session.session_key
    if not session_key:
        session_key = request.session.cycle_key()

    return render(request, 'products/product.html', locals())

