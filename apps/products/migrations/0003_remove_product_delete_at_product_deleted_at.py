# Generated by Django 5.1.1 on 2024-09-21 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_alter_product_state"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="delete_at",
        ),
        migrations.AddField(
            model_name="product",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
    ]