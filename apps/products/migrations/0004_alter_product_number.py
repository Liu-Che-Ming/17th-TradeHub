# Generated by Django 5.1.1 on 2024-09-22 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_remove_product_delete_at_product_deleted_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="number",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]