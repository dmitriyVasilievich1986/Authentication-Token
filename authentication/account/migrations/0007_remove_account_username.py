# Generated by Django 3.1.5 on 2021-01-04 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20210104_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='username',
        ),
    ]
