# Generated by Django 3.1.4 on 2021-01-06 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0012_listing_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='engine',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
