# Generated by Django 3.2.1 on 2022-02-17 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_error_banner_popup_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/partners')),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'Partners',
            },
        ),
        migrations.CreateModel(
            name='Admin_Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/reviews')),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'Admin_Reviews',
            },
        ),
    ]
