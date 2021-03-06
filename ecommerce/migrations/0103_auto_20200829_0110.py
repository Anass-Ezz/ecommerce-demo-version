# Generated by Django 3.0.8 on 2020-08-29 00:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0102_auto_20200828_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.Order'),
        ),
        migrations.AlterField(
            model_name='product',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 29, 1, 10, 29, 124175)),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.Order'),
        ),
    ]
