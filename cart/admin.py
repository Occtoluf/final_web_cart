from django.contrib import admin

from cart.models import Order, OrderLine


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('status',)


@admin.register(OrderLine)
class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('number_of_products', 'product_price', 'position')