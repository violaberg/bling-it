from django.contrib import admin
from .models import Gemstone, Category


class GemstoneAdmin(admin.ModelAdmin):
    """
    Admin configuration for Gemstone model.

    This class defines the admin interface for the Gemstone model,
    specifying how Gemstone objects are displayed in the Django admin.
    """
    list_display = (
        'sku',
        'name',
        'category',
        'cut',
        'clarity',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for Category model.

    This class defines the admin interface for the Category model,
    specifying how Category objects are displayed in the Django admin.
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Gemstone, GemstoneAdmin)
admin.site.register(Category, CategoryAdmin)
