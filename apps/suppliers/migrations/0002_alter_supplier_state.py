# Generated by Django 5.1.1 on 2024-09-17 15:54


import django_fsm
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("suppliers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="supplier",
            name="state",
            field=django_fsm.FSMField(
                choices=[
                    ("often", "經常購買"),
                    ("haply", "偶爾購買"),
                    ("never", "未購買"),
                ],
                default="never",
                max_length=50,
                protected=True,
            ),
        ),
    ]
