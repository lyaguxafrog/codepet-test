# Generated by Django 5.0.3 on 2024-04-03 08:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_userprofile_create_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="create_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now,
                verbose_name="Дата создания пользователя",
            ),
        ),
    ]
