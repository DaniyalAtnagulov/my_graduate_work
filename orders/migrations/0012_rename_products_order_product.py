# Generated by Django 4.1.11 on 2024-04-21 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_remove_order_product_order_products_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='products',
            new_name='product',
        ),
    ]