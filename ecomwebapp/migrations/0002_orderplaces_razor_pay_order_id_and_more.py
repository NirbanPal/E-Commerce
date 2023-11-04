# Generated by Django 4.1.5 on 2023-02-18 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecomwebapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderplaces",
            name="razor_pay_order_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="orderplaces",
            name="razor_pay_payment_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="orderplaces",
            name="razor_pay_payment_signature",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]