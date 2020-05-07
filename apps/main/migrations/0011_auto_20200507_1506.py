# Generated by Django 3.0.6 on 2020-05-07 22:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200507_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='config',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
