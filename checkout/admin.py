from django.contrib import admin
from .models import Order, OrderLineItem, OrderStatus


# Register your models here.
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderStatusAdminInline(admin.TabularInline):
    model = OrderStatus
    readonly_fields = ('order',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline, OrderStatusAdminInline,)

    readonly_fields = ('order_number', 'date', 'total',
                       'grand_total', 'original_bag', 'stripe_pid',)
    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country', 'postcode',
              'town_or_city', 'street_address1', 'street_address2',
              'county', 'total', 'grand_total', 'original_bag', 'stripe_pid',
              )

    list_display = ('order_number', 'date', 'full_name',
                    'total', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
