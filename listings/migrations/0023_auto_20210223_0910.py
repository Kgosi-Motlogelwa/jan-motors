# Generated by Django 3.0.5 on 2021-02-23 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0022_merge_20210218_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='contact_number',
            field=models.CharField(default='71 389 656', max_length=2002),
        ),
    ]
