# Generated by Django 3.1.3 on 2020-12-16 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dukaapp', '0002_user_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]
