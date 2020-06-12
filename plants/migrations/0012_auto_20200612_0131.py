# Generated by Django 3.0.5 on 2020-06-11 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0011_auto_20200609_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='last_cutting_date',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='last_manuring_date',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='last_watering_date',
        ),
        migrations.AddField(
            model_name='associative_gardens',
            name='last_cutting_date',
            field=models.DateField(default='2000-11-11'),
        ),
        migrations.AddField(
            model_name='associative_gardens',
            name='last_manuring_date',
            field=models.DateField(default='2000-11-11'),
        ),
        migrations.AddField(
            model_name='associative_gardens',
            name='last_watering_date',
            field=models.DateField(default='2000-11-11'),
        ),
    ]
