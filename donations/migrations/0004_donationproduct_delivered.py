# Generated by Django 3.1.1 on 2020-10-29 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0003_donation_payment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationproduct',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
    ]