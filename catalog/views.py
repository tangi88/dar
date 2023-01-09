from django.core.paginator import Paginator
from django.shortcuts import render
from products.models import Product, ProductImage
from cart.forms import CartAddProductForm
from cart.cart import Cart


def catalog(request):
    products_images = []
    products = Product.objects.all()
    paginator = Paginator(products, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    cart = Cart(request)
    cart_add_form = CartAddProductForm(initial={'quantity': 1})

    for product in page_obj:
        images = ProductImage.objects.filter(product=product).order_by('-is_main')
        image = images[0].image if images.exists() else None

        products_images.append({'product': product, 'image': image})

    return render(request, 'catalog/catalog.html', {'products_images': products_images,
                                                    'cart': cart,
                                                    'cart_add_form': cart_add_form,
                                                    'page_obj': page_obj})

