# Generated by Django 5.1 on 2024-08-29 05:01

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Inventory",
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
                ("product", models.CharField(max_length=255)),
                ("supplier", models.CharField(max_length=255)),
                ("quantity", models.IntegerField()),
                ("safety_stock", models.IntegerField(null=True)),
                ("last_updated", models.DateTimeField(auto_now_add=True)),
                ("note", models.TextField(blank=True)),
            ],
        ),
    ]
