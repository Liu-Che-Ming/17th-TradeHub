# Generated by Django 5.1.1 on 2024-09-08 01:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("goods_receipts", "0001_initial"),
        ("products", "0002_alter_product_price_alter_product_product_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="goodsreceipt",
            name="goods_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="goods_receipts",
                to="products.product",
            ),
        ),
        migrations.AlterField(
            model_name="goodsreceipt",
            name="quantity",
            field=models.PositiveIntegerField(),
        ),
    ]
