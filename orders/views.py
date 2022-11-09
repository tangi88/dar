from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import ProductInBasket, Order, OrderProduct
from .forms import CheckoutContactForm
from .serializers import OrderSerializer


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key

    data = request.POST
    product_id = data.get('product_id')
    nmb = data.get('nmb')
    is_delete = data.get('is_delete')

    if is_delete == 'true':
        ProductInBasket.objects.filter(id=product_id).delete()
    else:
        # new_product = ProductInBasket.objects.create(session_key=session_key, product_id=product_id, amount=nmb)
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id, defaults={'amount': nmb})
        if not created:
            new_product.amount += int(nmb)
            new_product.save(force_update=True)

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key)
    return_dict['products_total'] = products_in_basket.count()
    return_dict['products'] = list()

    for product_in_basket in products_in_basket:
        product_dict = dict()
        product_dict['id'] = product_in_basket.id
        product_dict['name'] = product_in_basket.product.name
        product_dict['price'] = product_in_basket.price
        product_dict['amount'] = product_in_basket.amount

        return_dict['products'].append(product_dict)

    return JsonResponse(return_dict)


def checkout(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key).exclude(order__isnull=False)
    form = CheckoutContactForm(request.POST or None)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            data = request.POST
            name = data.get('name')
            phone = data['phone']
            user, created = User.objects.get_or_create(username=phone, defaults={'first_name': name})

            order = Order.objects.create(user=user, customer_name=name, customer_phone=phone)

            for name, value in data.items():
                if name.startswith('product_basket_'):
                    product_basket_id = name.split('product_basket_')[1]
                    product_basket = ProductInBasket.objects.get(id=product_basket_id)
                    product_basket.order = order
                    product_basket.amount = int(value)
                    product_basket.save(force_update=True)

                    OrderProduct.objects.create(order=order,
                                                product=product_basket.product, amount=product_basket.amount,
                                                price=product_basket.price)
        else:
            print('no')
    return render(request, 'orders/checkout.html', locals())


# class OrderAPIView(APIView):
#     def get(self, request):
#         o = Order.objects.all()
#         return Response({'orders': OrderSerializer(o, many=True).data})
#
#     def post(self, request):
#         serializer = OrderSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'order': serializer.data})
#         # order_new = Order.objects.create(
#         #
#         # )
#         #
#         # return Response({'order': OrderSerializer(order_new).data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT not allowed'})
#
#         try:
#             instance = Order.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exists'})
#
#         serializer = OrderSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'order': serializer.data})


# class OrderAPIView(generics.ListAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
#
# class OrderAPIUpdate(generics.UpdateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

class OrderViewSet(mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
# class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
