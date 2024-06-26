# Generated by Django 5.0.3 on 2024-04-03 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fundraising", "0003_delete_donaterslist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collect",
            name="status",
            field=models.BooleanField(
                default=True,
                help_text="True - сбор активен, False - нет",
                verbose_name="Статус сбора",
            ),
        ),
    ]
