# Generated by Django 5.0.6 on 2024-07-04 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='clothes', verbose_name='image')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=7, verbose_name='price')),
                ('discount', models.SmallIntegerField(blank=True, default=0, verbose_name='discount')),
                ('uploaded', models.DateTimeField(auto_now_add=True, verbose_name='uploaded date')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clothes', to='shop.category')),
            ],
            options={
                'verbose_name_plural': 'Clothes',
            },
        ),
    ]
