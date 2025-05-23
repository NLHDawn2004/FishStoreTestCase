# Generated by Django 5.0.3 on 2024-03-19 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_remove_cart_product_remove_cart_quantity_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='endow',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]
