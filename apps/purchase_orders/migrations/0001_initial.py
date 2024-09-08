# Generated by Django 5.1.1 on 2024-09-04 08:30


import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("suppliers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PurchaseOrder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order_number", models.CharField(max_length=20, unique=True)),
                (
                    "supplier_tel",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "contact_person",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "supplier_email",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                ("order_date", models.DateField(default=django.utils.timezone.now)),
                ("total_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("notes", models.TextField(blank=True, null=True)),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="purchase_orders",
                        to="suppliers.supplier",
                    ),
                ),
            ],
        ),
    ]
