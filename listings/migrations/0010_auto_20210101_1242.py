# Generated by Django 3.1.4 on 2021-01-01 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_auto_20210101_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='mileage',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='transmission',
            field=models.CharField(choices=[('Automatic', 'Auto'), ('Manual', 'Manual')], default='Transmission (All)', max_length=20),
        ),
    ]
