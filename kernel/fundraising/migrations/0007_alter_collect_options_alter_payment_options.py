# Generated by Django 5.0.3 on 2024-04-03 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fundraising", "0006_alter_payment_pay_to_alter_payment_payer"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="collect",
            options={"verbose_name": "Сборы"},
        ),
        migrations.AlterModelOptions(
            name="payment",
            options={"verbose_name": "Платеж", "verbose_name_plural": "Платежи"},
        ),
    ]
