# Generated by Django 3.2.1 on 2022-02-22 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_delete_configuration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='country',
            new_name='country_vendor',
        ),
        migrations.AddField(
            model_name='user',
            name='Address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='City',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='Country_cus',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='Fax',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='Zip',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
