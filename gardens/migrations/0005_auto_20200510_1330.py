# Generated by Django 3.0.5 on 2020-05-10 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gardens', '0004_garden_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garden',
            name='id_user',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
