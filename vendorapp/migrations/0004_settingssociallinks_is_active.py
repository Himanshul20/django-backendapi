# Generated by Django 3.2.1 on 2022-02-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendorapp', '0003_settingsbanner_settingsservices_settingssociallinks'),
    ]

    operations = [
        migrations.AddField(
            model_name='settingssociallinks',
            name='is_active',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
