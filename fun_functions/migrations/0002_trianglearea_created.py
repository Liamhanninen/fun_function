# Generated by Django 3.0.3 on 2020-09-14 20:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fun_functions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trianglearea',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
    ]
