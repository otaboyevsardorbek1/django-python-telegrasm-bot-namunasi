# Generated by Django 3.1 on 2022-10-04 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_order_entities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='current_utrl',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]
