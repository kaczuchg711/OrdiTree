# Generated by Django 3.0.5 on 2020-06-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gardens', '0006_auto_20200510_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garden',
            name='id_user',
            field=models.IntegerField(),
        ),
    ]
