# Generated by Django 3.2.1 on 2022-02-08 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20220208_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_category',
            name='Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sub_category',
            name='Name',
            field=models.CharField(max_length=100),
        ),
    ]