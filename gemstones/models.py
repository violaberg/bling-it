from django.db import models
from decimal import Decimal
import datetime


# Create your models here.
class Category (models.Model):
    """
    Represents a category for gemstones in the shop.

    Attributes:
        name (str): The name of the category.
        friendly_name (str): User friendly name for the category (optional).

    Methods:
        __str__: Returns the name of the category as a string representation.
        get_friendly_name: Returns the friendly name of the category.
    """

    class Meta:
        """
        Customizes the display name of the category in the admin panel.
        """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Gemstone (models.Model):
    """
    Represents a gemstone available in the shop.

    Attributes:
        category (Category): The category to which the gemstone belongs.
        sku (str): The stock keeping unit (SKU) code of the gemstone.
        name (str): The name of the gemstone.
        description (str): The detailed description of the gemstone.
        color (str): The color of the gemstone.
        cut (str): The cut or shape of the gemstone.
        carats (Decimal): The weight of the gemstone in carats.
        treatment (str): The treatment applied to the gemstone.
        certification (str): The certification authority of the gemstone.
        origin (str): The origin or source of the gemstone.
        price (Decimal): The price of the gemstone.
        image_url (str): The link to an external image of the gemstone (optional).
        image (ImageField): The image of the gemstone stored locally (optional).

    Methods:
        __str__: Returns the name of the gemstone as a string representation.
    """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(
        max_length=254, null=True, blank=True)
    name = models.CharField(
        max_length=254)
    description = models.TextField()
    color = models.CharField(
        max_length=20)
    cut = models.CharField(
        max_length=20)
    clarity = models.CharField(
        max_length=20, default='')
    carats = models.DecimalField(
        max_digits=6, decimal_places=2)
    treatment = models.CharField(
        max_length=20)
    certification = models.CharField(
        max_length=20)
    origin = models.CharField(
        max_length=100)
    price = models.DecimalField(
        max_digits=10, decimal_places=2)
    image_url = models.URLField(
        max_length=1024, null=True, blank=True)
    image = models.ImageField(
        null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return self.name
