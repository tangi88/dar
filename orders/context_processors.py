from .models import ProductInBasket


def getting_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        session_key = request.session.cycle_key()

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, order__isnull=True)
    products_total = products_in_basket.count()

    return locals()

