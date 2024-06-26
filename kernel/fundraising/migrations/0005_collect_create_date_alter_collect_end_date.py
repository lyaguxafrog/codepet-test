# Generated by Django 5.0.3 on 2024-04-03 02:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fundraising", "0004_alter_collect_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="collect",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime.now, verbose_name="Дата создания сбора"
            ),
        ),
        migrations.AlterField(
            model_name="collect",
            name="end_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="дата конца сбора средств"
            ),
        ),
    ]
