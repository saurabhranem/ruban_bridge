# Generated by Django 2.0.9 on 2018-11-08 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruban', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
