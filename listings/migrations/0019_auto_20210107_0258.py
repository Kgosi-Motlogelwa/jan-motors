# Generated by Django 3.1.4 on 2021-01-07 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0018_auto_20210107_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='mileage',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]