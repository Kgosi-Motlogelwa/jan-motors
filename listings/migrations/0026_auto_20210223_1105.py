# Generated by Django 3.0.5 on 2021-02-23 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0025_auto_20210223_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='photo_10',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_7',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_8',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='photo_9',
        ),
    ]
