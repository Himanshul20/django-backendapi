# Generated by Django 3.2.1 on 2022-02-17 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_footer_content_order_pickup_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Error_Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/banner')),
            ],
            options={
                'db_table': 'Error_Banner',
            },
        ),
        migrations.CreateModel(
            name='Popup_Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(blank=True, null=True)),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='media/banner')),
                ('popup_title', models.CharField(blank=True, max_length=1000, null=True)),
                ('popup_text', models.TextField(blank=True, max_length=10000, null=True)),
            ],
            options={
                'db_table': 'Popup_Banner',
            },
        ),
    ]
