# Generated by Django 3.2.1 on 2022-02-21 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_configuration'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Configuration',
        ),
    ]
