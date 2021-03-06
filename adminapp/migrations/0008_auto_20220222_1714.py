# Generated by Django 3.2.1 on 2022-02-22 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_admin_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loaders',
            name='Admin_Loader',
            field=models.ImageField(blank=True, default='', null=True, upload_to='media/Loader/'),
        ),
        migrations.AlterField(
            model_name='loaders',
            name='Status',
            field=models.CharField(blank=True, choices=[('Activated', 'Activated'), ('Deactivated', 'Deactivated')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='loaders',
            name='Website_Loader',
            field=models.ImageField(blank=True, default='', null=True, upload_to='media/Loader/'),
        ),
    ]
