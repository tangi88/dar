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
from orders.views import *
from products.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
    path('', include('indexpage.urls')),
    path('', include('products.urls')),
    path('', include('services.urls')),
    path('', include('prices.urls')),
    path('', include('catalog.urls')),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/productlist/', ProductAPIView.as_view()),
    path('api/v1/unitlist/', ProductUnitAPIView.as_view()),
    path('api/v1/categorylist/', ProductCategoryAPIView.as_view()),
    path('api/v1/productimagelist/', ProductImageAPIView.as_view()),
    path('api/v1/orderlist/<int:pk>/', OrderAPIView.as_view()),
    path('api/v1/orderlist/', OrderAPIView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__', include(debug_toolbar.urls))
    ]

