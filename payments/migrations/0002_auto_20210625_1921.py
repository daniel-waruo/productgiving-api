# Generated by Django 3.2.4 on 2021-06-25 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaignfeetransaction',
            name='transaction_id',
        ),
        migrations.RemoveField(
            model_name='donationtransaction',
            name='transaction_id',
        ),
        migrations.AddField(
            model_name='campaignfeetransaction',
            name='checkout_request_id',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='campaignfeetransaction',
            name='merchant_request_id',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='donationtransaction',
            name='checkout_request_id',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='donationtransaction',
            name='merchant_request_id',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='campaignfeetransaction',
            name='mpesa_code',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='donationtransaction',
            name='mpesa_code',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
    ]
