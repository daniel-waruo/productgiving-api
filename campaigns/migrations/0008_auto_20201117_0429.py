# Generated by Django 3.1.1 on 2020-11-17 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0007_auto_20201105_0606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campaignproduct',
            options={'ordering': ('product',)},
        ),
        migrations.AddField(
            model_name='campaignproduct',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
