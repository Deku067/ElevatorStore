# Generated by Django 5.0.2 on 2024-06-01 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('User', 'User')], default='User', max_length=5),
        ),
    ]
