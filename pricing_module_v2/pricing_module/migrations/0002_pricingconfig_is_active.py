# Generated by Django 4.2.3 on 2023-07-23 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pricing_module", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pricingconfig",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]