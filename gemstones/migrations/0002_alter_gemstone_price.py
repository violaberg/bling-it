# Generated by Django 3.2.25 on 2024-04-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gemstones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gemstone',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
