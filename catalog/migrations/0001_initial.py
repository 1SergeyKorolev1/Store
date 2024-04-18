# Generated by Django 5.0.4 on 2024-04-18 10:06

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
                ('name', models.CharField(max_length=150, verbose_name='название')),
                ('description', models.CharField(blank=True, max_length=150, null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('description', models.CharField(blank=True, max_length=150, null=True, verbose_name='описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='img_product', verbose_name='изображение')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='цена')),
                ('created_at', models.DateField(verbose_name='дата создания')),
                ('updated_at', models.DateField(verbose_name='дата обновления')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
