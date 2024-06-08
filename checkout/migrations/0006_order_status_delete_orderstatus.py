# Generated by Django 4.2.7 on 2024-06-07 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('in_progress', 'In Progress'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='in_progress', max_length=20),
        ),
        migrations.DeleteModel(
            name='OrderStatus',
        ),
    ]