# Generated by Django 3.0.4 on 2020-03-28 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_auto_20200327_0812'),
        ('votes', '0002_auto_20200327_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='candidate',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='candidates.Candidate'),
        ),
    ]