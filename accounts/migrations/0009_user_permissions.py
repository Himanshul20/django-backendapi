# Generated by Django 3.2.1 on 2022-02-17 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_admin_coupon_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='permissions',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
