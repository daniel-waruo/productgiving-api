# Generated by Django 3.1.1 on 2020-09-22 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200922_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
    ]
