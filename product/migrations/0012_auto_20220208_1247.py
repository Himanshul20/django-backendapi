# Generated by Django 3.2.1 on 2022-02-08 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20220208_1231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_product',
            old_name='sub_category',
            new_name='subcategory',
        ),
        migrations.RemoveField(
            model_name='sub_category',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='sub_category',
            name='Slug',
        ),
        migrations.AddField(
            model_name='sub_category',
            name='name',
            field=models.CharField(db_index=True, default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sub_category',
            name='slug',
            field=models.SlugField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='add_product',
            name='Name',
            field=models.CharField(db_index=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='add_product',
            name='Slug',
            field=models.CharField(db_index=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='main_category',
            name='Name',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='main_category',
            name='Slug',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
