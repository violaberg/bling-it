# Generated by Django 4.2.7 on 2024-06-09 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gemstones', '0005_gemstone_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gemstone',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
