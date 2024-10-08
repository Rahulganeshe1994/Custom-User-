# Generated by Django 5.1 on 2024-08-26 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='user_profile'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
