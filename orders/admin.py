from django.contrib import admin
from .models import Order, OrderProduct, ProductInBasket


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [OrderProductInline]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class OrderProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderProduct._meta.fields]

    class Meta:
        model = OrderProduct


admin.site.register(OrderProduct, OrderProductAdmin)


class ProductInBasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]

    class Meta:
        model = ProductInBasket


admin.site.register(ProductInBasket, ProductInBasketAdmin)

