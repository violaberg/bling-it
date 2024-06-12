from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

from gemstones.models import Gemstone


class UserProfile(models.Model):
    """
    A user profile model for maintaining order history,
    default delivery information and wishlist
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_county = models.CharField(
        max_length=80, null=True, blank=True)
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(
        sender, instance, created, **kwargs):
    """
    Signal receiver function to create or update the user profile.

    If a new user is created, create a corresponding UserProfile instance.
    For existing users, save the UserProfile instance.

    Args:
        sender (Model): The model class that sent the signal.
        instance (User): The instance of the User model.
        created (bool): A boolean indicating if the user is newly created.
        **kwargs: Additional keyword arguments.
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()


class Wishlist(models.Model):
    """
    Model for user wishlists.

    Each user can have multiple gemstones in their wishlist.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    gemstones = models.ManyToManyField(
        Gemstone, related_name='wishlists')
    created = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return f"Wishlist for {self.user.username}"
