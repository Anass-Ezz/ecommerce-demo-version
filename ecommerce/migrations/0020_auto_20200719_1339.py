# Generated by Django 3.0.8 on 2020-07-19 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0019_order_add_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Varient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VarientName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('varient', models.ManyToManyField(to='ecommerce.Varient')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='varient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.VarientName'),
        ),
    ]
