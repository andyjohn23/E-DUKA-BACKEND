# Generated by Django 3.1.3 on 2021-01-12 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dukaapp', '0004_auto_20210112_0856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='shop',
        ),
        migrations.AlterField(
            model_name='product',
            name='shipped_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop', to='dukaapp.shop'),
        ),
    ]
