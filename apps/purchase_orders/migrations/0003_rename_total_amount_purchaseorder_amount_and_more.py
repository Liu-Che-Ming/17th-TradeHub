# Generated by Django 5.1.1 on 2024-09-21 08:59

import django_fsm
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "purchase_orders",
            "0002_purchaseorder_deleted_at_purchaseorder_state_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="purchaseorder",
            old_name="total_amount",
            new_name="amount",
        ),
        migrations.RenameField(
            model_name="purchaseorder",
            old_name="notes",
            new_name="note",
        ),
        migrations.AddField(
            model_name="purchaseorder",
            name="is_finished",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="purchaseorder",
            name="username",
            field=models.CharField(default="admin", max_length=150),
        ),
        migrations.AlterField(
            model_name="purchaseorder",
            name="state",
            field=django_fsm.FSMField(
                choices=[
                    ("pending", "待處理"),
                    ("progress", "進行中"),
                    ("finished", "已完成"),
                ],
                default="progress",
                max_length=50,
                protected=True,
            ),
        ),
    ]
