# Generated by Django 3.0.8 on 2020-07-15 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_auto_20200715_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(to='ecommerce.ProductImage'),
        ),
        migrations.DeleteModel(
            name='ProductImageBandle',
        ),
    ]
