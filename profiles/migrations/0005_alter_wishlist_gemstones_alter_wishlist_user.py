# Generated by Django 4.2.7 on 2024-06-08 22:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gemstones', '0004_gemstone_clarity'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0004_rename_gemstone_wishlist_gemstones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='gemstones',
            field=models.ManyToManyField(related_name='wishlists', to='gemstones.gemstone'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
