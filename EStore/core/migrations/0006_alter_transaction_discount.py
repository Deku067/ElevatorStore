# Generated by Django 5.0.2 on 2024-06-01 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='discount',
            field=models.PositiveIntegerField(blank=True, max_length=2, null=True),
        ),
    ]