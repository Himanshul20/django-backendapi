# Generated by Django 3.2.1 on 2022-02-12 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendorapp', '0008_auto_20220210_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='user',
        ),
    ]