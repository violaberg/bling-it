import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField

from gemstones.models import Gemstone
from profiles.models import UserProfile


STATUS = (
    ('in_progress', 'In Progress'),
    ('delivered', 'Delivered'),
    ('cancelled', 'Cancelled'),
)


class Order(models.Model):
    """
    Represents an order placed by a user in the e-commerce system.

    Attributes:
        order_number (str): A unique identifier for the order.
        user_profile (UserProfile): The user profile associated with this order.
        full_name (str): The full name of the person who placed the order.
        email (str): The email address of the person who placed the order.
        phone_number (str): The phone number of the person who placed the order.
        country (CountryField): The country to which the order will be shipped.
        postcode (str): The postal code for the shipping address.
        town_or_city (str): The town or city for the shipping address.
        street_address1 (str): The primary street address.
        street_address2 (str): The secondary street address (optional).
        county (str): The county, state, or region for the shipping address (optional).
        date (datetime): The date and time when the order was placed.
        total (decimal): The total cost of the order before additional charges.
        grand_total (decimal): The final total cost of the order, including additional charges.
        original_bag (str): A JSON representation of the original bag contents.
        stripe_pid (str): The Stripe Payment Intent ID for the order.
        status (str): The current status of the order (e.g., in progress, delivered, cancelled).
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='orders'
        )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
        )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
        )
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=''
        )
    status = models.CharField(
        max_length=20, choices=STATUS, default='in_progress')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID.

        Returns:
            str: A unique order number consisting of uppercase hexadecimal digits.
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update the grand total of the order each time a line item is added or updated.

        This method aggregates the total cost of all associated line items and updates
        the `total` and `grand_total` fields of the order.
        """
        self.total = self.lineitems.aggregate(
            Sum('lineitem_total')
            )['lineitem_total__sum'] or 0
        self.grand_total = self.total
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number if it hasn't been set already.

        This ensures that every order has a unique identifier before it is saved to the database.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    Represents an individual line item within an order.

    Attributes:
        order (Order): The order to which this line item belongs.
        gemstone (Gemstone): The gemstone associated with this line item.
        lineitem_total (decimal): The total cost of this line item.
    """
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems'
        )
    gemstone = models.ForeignKey(
        Gemstone, null=False, blank=False, on_delete=models.CASCADE
        )
    lineitem_total = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=False, blank=False, editable=False
        )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total and update the order total.

        This ensures that the cost of the line item is calculated based on the price of the gemstone
        and that the order's total is updated accordingly.
        """
        self.lineitem_total = self.gemstone.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.gemstone.sku} on order {self.order.order_number}'
