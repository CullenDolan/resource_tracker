# Generated by Django 2.2 on 2021-04-10 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resource_app', '0004_auto_20210410_0855'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Building',
            new_name='Location',
        ),
    ]
