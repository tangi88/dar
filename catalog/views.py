from django.shortcuts import render
from products.models import Product, ProductImage
from cart.forms import CartAddProductForm
from cart.cart import Cart


def catalog(request):
    products_images = []
    products = Product.objects.all()
    cart = Cart(request)
    cart_add_form = CartAddProductForm(initial={'quantity': 1})

    for product in products:
        image = ProductImage.objects.filter(product=product).order_by('-is_main')
        image_path = image[0].image.url if image.exists() else '/'

        products_images.append({'product': product, 'image': image_path})

    return render(request, 'catalog/catalog.html', {'products_images': products_images,
                                                    'cart': cart,
                                                    'cart_add_form': cart_add_form})

