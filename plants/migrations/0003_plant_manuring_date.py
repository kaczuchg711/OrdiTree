# Generated by Django 3.0.5 on 2020-06-08 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_plant_temperature'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='manuring_date',
            field=models.DateField(default='2000-11-11'),
        ),
    ]
