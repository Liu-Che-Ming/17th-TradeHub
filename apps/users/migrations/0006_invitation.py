# Generated by Django 5.1.1 on 2024-09-23 08:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("company", "0007_rename_company_name_company_name"),
        ("users", "0005_alter_customuser_company"),
    ]

    operations = [
        migrations.CreateModel(
            name="Invitation",
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
                ("email", models.EmailField(max_length=254)),
                ("token", models.CharField(max_length=50, unique=True)),
                ("is_used", models.BooleanField(default=False)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company.company",
                    ),
                ),
            ],
        ),
    ]