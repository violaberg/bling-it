from django.contrib import admin
from .models import Gemstone, Category


class GemstoneAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'cut',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Gemstone, GemstoneAdmin)
admin.site.register(Category, CategoryAdmin)
