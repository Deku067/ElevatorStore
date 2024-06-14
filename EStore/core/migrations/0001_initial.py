# Generated by Django 5.0.2 on 2024-06-14 14:31

import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('prof', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('kind', models.CharField(max_length=255)),
                ('count', models.PositiveIntegerField()),
                ('manufacturer', models.CharField(choices=[('USA', 'United States'), ('UK', 'United Kingdom'), ('CN', 'China'), ('JP', 'Japan'), ('IR', 'Iran'), ('DE', 'Germany'), ('SE', 'Sweden'), ('IT', 'Italy'), ('CH', 'Switzerland'), ('NO', 'Norway'), ('CA', 'Canada'), ('FI', 'Finland'), ('RU', 'Russia')], default='IR', max_length=3)),
                ('category', models.CharField(choices=[('PART', 'Parts'), ('SHP', 'Second Hand Parts'), ('CON', 'Contract')], default='PART', max_length=4)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(blank=True, to='core.product')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='prof.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, default=Decimal('0.0'), max_digits=10)),
                ('discount', models.PositiveIntegerField(blank=True, null=True)),
                ('purchase', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.purchase')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='prof.userprofile')),
            ],
        ),
    ]
