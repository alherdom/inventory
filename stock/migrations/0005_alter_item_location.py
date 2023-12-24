# Generated by Django 5.0 on 2023-12-24 10:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_alter_item_location_alter_item_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='stock.location'),
        ),
    ]
