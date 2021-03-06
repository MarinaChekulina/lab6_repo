# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-11 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('adr', models.CharField(max_length=255, verbose_name='Адрес')),
                ('time', models.CharField(max_length=255, verbose_name='Время работы')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название модели автомобиля')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('country', models.CharField(max_length=100, verbose_name='Страна-производитель')),
                ('image_car', models.ImageField(upload_to='images', verbose_name='Изображение модели')),
                ('length', models.CharField(max_length=20, verbose_name='Длина автомобиля')),
                ('vehicle_clearance', models.CharField(max_length=15, verbose_name='Клиренс автомобиля')),
                ('max_speed', models.CharField(max_length=15, verbose_name='Максимальная скорость автомобиля')),
                ('average_fuel_consumption', models.CharField(max_length=15, verbose_name='Средний расход топлива в смешанном режиме')),
                ('weight', models.CharField(max_length=15, verbose_name='Масса автомобиля')),
                ('type_of_transmission', models.CharField(max_length=100, verbose_name='Коробка передач')),
                ('volume', models.CharField(max_length=20, verbose_name='Объем двигателя')),
                ('description', models.CharField(max_length=1500, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('date', models.CharField(max_length=50, verbose_name='Сроки акции')),
                ('text', models.CharField(max_length=255, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dop_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('phone', models.CharField(max_length=20, verbose_name='Контактный телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
            ],
        ),
    ]
