# Generated by Django 3.0.5 on 2021-03-03 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0027_auto_20210302_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='dealership',
            field=models.CharField(choices=[('Gaborone', 'Gaborone'), ('Palapye', 'Palapye'), ('Francistown', 'Francistown')], default='Dealership (All)', max_length=20),
        ),
    ]