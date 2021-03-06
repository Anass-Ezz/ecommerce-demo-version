# Generated by Django 3.0.8 on 2020-08-13 16:21

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0070_auto_20200812_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.Order'),
        ),
        migrations.AlterField(
            model_name='product',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 17, 21, 39, 934186)),
        ),
        migrations.AlterField(
            model_name='sippingadress',
            name='country',
            field=django_countries.fields.CountryField(blank=True, default='Morocco', max_length=2, null=True),
        ),
    ]
