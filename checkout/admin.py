from django.contrib import admin
from .models import Order, OrderItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('order_item_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_id', 'date', 'delivery_price', 'order_total', 'grand_total', 'original_bag', 'stripe_pid')


    fields = ('order_id', 'name', 'user_profile', 'email', 'phone', 'street_address1',
              'street_address2', 'city', 'county',
              'country', 'postcode', 'delivery_price',
              'order_total', 'grand_total', 'date', 'original_bag', 'stripe_pid')

    list_display = ('order_id', 'date', 'name',
                    'order_total', 'delivery_price',
                    'grand_total',)


    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)   