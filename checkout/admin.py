from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Inline admin for order line items.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Admin interface for orders.
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'total',
                       'grand_total', 'original_bag', 'stripe_pid',)
    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country', 'postcode',
              'town_or_city', 'street_address1', 'street_address2',
              'county', 'total', 'grand_total', 'original_bag', 'stripe_pid',
              'status',)

    list_display = ('order_number', 'date', 'full_name',
                    'total', 'grand_total', 'status',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
