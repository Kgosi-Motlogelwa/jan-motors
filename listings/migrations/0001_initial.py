# Generated by Django 3.1.4 on 2020-12-25 07:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('brand_model', models.CharField(choices=[('Alfa Romeo', 'Alfa Romeo'), ('Audi', 'Audi'), ('BMW', 'BMW'), ('Chevrolet', 'Chevrolet'), ('Chrysler', 'Chrysler'), ('Citroen', 'Citroen'), ('Dodge', 'Dodge'), ('Fiat', 'Fiat'), ('Ford', 'Ford'), ('Honda', 'Honda'), ('Hyundai', 'Hyundai'), ('Isuzu', 'Isuzu'), ('Jaguar', 'Jaguar'), ('Jeep', 'Jeep'), ('Kia', 'Kia'), ('Land Rover', 'Land Rover'), ('Lexus', 'Lexus'), ('Mazda', 'Mazda'), ('Mercedes Benz', 'Mercedes Benz'), ('Mini', 'Mini'), ('Mitsubishi', 'Mitsubishi'), ('Nissan', 'Nissan'), ('Opel', 'Opel'), ('Peugeot', 'Peugeot'), ('Subaru', 'Subaru'), ('Suzuki', 'Suzuki'), ('Toyota', 'Toyota'), ('Volkswagen', 'Volkswagen'), ('Volvo', 'Volvo')], max_length=50)),
                ('transmission', models.CharField(max_length=20)),
                ('fuel_type', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('mileage', models.IntegerField()),
                ('year', models.IntegerField()),
                ('dealership', models.CharField(max_length=20)),
                ('body_type', models.CharField(max_length=20)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/ %m/%d')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('photo_7', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
