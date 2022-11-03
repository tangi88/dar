from django.urls import path
from . import views


urlpatterns = [
    path('product/<int:product_id>', views.product, name='product'),
    # path(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
    # path('', views.index_page),
]

