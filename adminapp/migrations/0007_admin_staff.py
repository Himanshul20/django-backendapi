# Generated by Django 3.2.1 on 2022-02-21 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_admin_partners_admin_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Staff_Profile_Image', models.ImageField(blank=True, default='', null=True, upload_to='media/staff')),
                ('Name', models.CharField(blank=True, max_length=500, null=True)),
                ('Email', models.EmailField(blank=True, max_length=2540, null=True)),
                ('Phone', models.CharField(blank=True, max_length=1000, null=True)),
                ('Role', models.CharField(blank=True, choices=[('Manager', 'Manager'), ('Moderator', 'Moderator'), ('Staff', 'Staff')], max_length=1000, null=True)),
                ('Password', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Admin_Staff',
            },
        ),
    ]