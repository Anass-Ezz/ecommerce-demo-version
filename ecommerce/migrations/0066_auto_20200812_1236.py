# Generated by Django 3.0.8 on 2020-08-12 11:36

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0065_auto_20200811_2310'),
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
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 12, 12, 36, 4, 864085)),
        ),
        migrations.AlterField(
            model_name='sippingadress',
            name='adresse_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sippingadress',
            name='adresse_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sippingadress',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='sippingadress',
            name='zip_code',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
