# Generated by Django 3.1.3 on 2020-12-30 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dukaapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='dukaapp.comment'),
        ),
    ]
