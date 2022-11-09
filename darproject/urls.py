"""darproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from orders.views import OrderViewSet
# from orders.views import OrderAPIView, OrderAPIUpdate
from products.views import ProductAPIDetailView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'order', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('indexpage.urls')),
    path('', include('products.urls')),
    path('', include('orders.urls')),
    path('api/v1/dar-auth/', include('rest_framework.urls')),
    path('api/v1/productlist/<int:pk>/', ProductAPIDetailView.as_view()),
    path('api/v1/', include(router.urls)),
    # path('api/v1/orderlist/', OrderViewSet.as_view({'get': 'list'})),
    # path('api/v1/orderlist/<int:pk>/', OrderViewSet.as_view({'put': 'update'})),
    # path('api/v1/orderlist/<int:pk>', OrderAPIView.as_view()),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__', include(debug_toolbar.urls))
    ]

