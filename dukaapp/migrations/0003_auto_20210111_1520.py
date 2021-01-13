# Generated by Django 3.1.3 on 2021-01-11 12:20

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dukaapp', '0002_auto_20210111_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image_2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image_3'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image_4'),
        ),
    ]