# Generated by Django 3.0.6 on 2020-05-05 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200505_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='sslexpire',
            field=models.DateField(default='1970-01-01'),
        ),
    ]