# Generated by Django 4.1.2 on 2022-10-18 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productcategory_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=1),
        ),
    ]
