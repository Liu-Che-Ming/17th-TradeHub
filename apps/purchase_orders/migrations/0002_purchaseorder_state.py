# Generated by Django 5.1.1 on 2024-09-12 00:05

import django_fsm
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("purchase_orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="purchaseorder",
            name="state",
            field=django_fsm.FSMField(
                choices=[("unfinish", "未完成"), ("finished", "完成")],
                default="unfinish",
                max_length=50,
                protected=True,
            ),
        ),
    ]