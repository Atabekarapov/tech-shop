from django.contrib import admin

from .models import Order, OrderItem


class OrderItemsInLine(admin.TabularInline):
    model = Order.items.through
    fields = ['products', 'quantity', 'price']
    readonly_fields = ['products', 'quantity', 'price']
    extra = 0

    def products(self, instance):
        return instance.orderitems

    def quantity(self, instance):
        return instance.orderitems.quantity

    def price(self, instance):
        return instance.orderitems.price


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemsInLine]
    exclude = ['items']
    list_display = (
        'id', 'user', 'status', 'created_at', 'total'
    )

admin.site.register(Order, OrderAdmin)