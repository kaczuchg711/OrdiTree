# Generated by Django 3.0.5 on 2020-05-10 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gardens', '0003_garden'),
    ]

    operations = [
        migrations.AddField(
            model_name='garden',
            name='id_user',
            field=models.IntegerField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
