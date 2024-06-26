# Generated by Django 5.0.3 on 2024-04-03 02:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fundraising", "0005_collect_create_date_alter_collect_end_date"),
        ("users", "0002_alter_userprofile_patronymic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="pay_to",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="fundraising.collect",
                verbose_name="Донат",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="payer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="users.userprofile",
                verbose_name="Донатер",
            ),
        ),
    ]
