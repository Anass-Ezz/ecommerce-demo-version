# Generated by Django 3.0.8 on 2020-08-13 19:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0074_auto_20200813_2024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sippingadress',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.Order'),
        ),
        migrations.AlterField(
            model_name='product',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 20, 25, 14, 925815)),
        ),
    ]
