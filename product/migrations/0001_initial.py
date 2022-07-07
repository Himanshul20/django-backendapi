# Generated by Django 3.2.1 on 2022-02-04 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Sku', models.TextField(default='', max_length=1000)),
                ('Name', models.CharField(max_length=100)),
                ('Slug', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Product_Stock', models.TextField(default='', max_length=1000)),
                ('Product_Description', models.TextField(default='', max_length=1000)),
                ('Product_Buy_Return_Policy', models.TextField(default='', max_length=1000)),
                ('featured_image', models.ImageField(upload_to='featured_image/')),
                ('Product_Current_Price', models.CharField(default='', max_length=100)),
                ('Product_Previous_Price', models.CharField(default='', max_length=100)),
                ('Tags', models.CharField(default='', max_length=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Configs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_logo', models.ImageField(blank=True, default='', null=True, upload_to='uploads/')),
                ('Footer_logo', models.ImageField(blank=True, default='', null=True, upload_to='uploads/')),
                ('Invoice_logo', models.ImageField(blank=True, default='', null=True, upload_to='uploads/')),
                ('Favicon', models.ImageField(blank=True, default='', null=True, upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Main_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Slug', models.CharField(max_length=100)),
                ('Status', models.CharField(choices=[('Active', 'Active'), ('Disabled', 'Disabled')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Main_category',
            },
        ),
        migrations.CreateModel(
            name='Sub_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Slug', models.CharField(max_length=100)),
                ('Status', models.CharField(choices=[('Active', 'Active'), ('Disabled', 'Disabled')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.main_category')),
            ],
            options={
                'db_table': 'Sub_category',
            },
        ),
        migrations.CreateModel(
            name='Product_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Gallery/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.add_product')),
            ],
            options={
                'db_table': 'Admin_Add_Product',
            },
        ),
        migrations.CreateModel(
            name='Child_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Slug', models.CharField(max_length=100)),
                ('Status', models.CharField(choices=[('Active', 'Active'), ('Disabled', 'Disabled')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.main_category')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.sub_category')),
            ],
            options={
                'db_table': 'Child_category',
            },
        ),
        migrations.AddField(
            model_name='add_product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.main_category'),
        ),
        migrations.AddField(
            model_name='add_product',
            name='child_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.child_category'),
        ),
        migrations.AddField(
            model_name='add_product',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.sub_category'),
        ),
    ]
