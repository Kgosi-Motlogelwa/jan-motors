# Generated by Django 3.1.4 on 2021-01-01 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20210101_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='available',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=50),
        ),
    ]