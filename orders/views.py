from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order, OrderProduct
from .forms import OrderCreateForm
from .serializers import OrderSerializer, OrderProductSerializer
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST' and len(cart) > 0:
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()

            for item in cart:
                OrderProduct.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             amount=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm

    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})


class OrderAPIView(APIView):
    def get(self, request):
        orders = Order.objects.filter(status__isnull=True)

        orders_data = []

        for order_obj in orders:
            dict_order = OrderSerializer(order_obj).data

            order_product_obj = OrderProduct.objects.filter(order=order_obj)
            products_data = []

            for product_order in order_product_obj:
                dict_product_order = OrderProductSerializer(product_order).data
                dict_product_order.update([('product_id_1c', product_order.product.id_1c)])

                products_data.append(dict_product_order)

            dict_order.update({'order_products': products_data})
            orders_data.append(dict_order)

        return Response({'orders': orders_data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Order.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists'})

        instance.status = 'unloaded'
        instance.save()

        return Response({'order': 'unloaded'})

