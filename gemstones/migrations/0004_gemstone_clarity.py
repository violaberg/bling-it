# Generated by Django 3.2.25 on 2024-04-19 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gemstones', '0003_remove_gemstone_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='gemstone',
            name='clarity',
            field=models.CharField(default='', max_length=20),
        ),
    ]
