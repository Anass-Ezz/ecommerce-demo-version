# Generated by Django 3.0.8 on 2020-07-19 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0021_auto_20200719_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='varientname',
            name='varient',
        ),
        migrations.AddField(
            model_name='varientname',
            name='varient',
            field=models.ManyToManyField(to='ecommerce.Varient'),
        ),
    ]
