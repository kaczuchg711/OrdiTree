# Generated by Django 3.0.5 on 2020-06-09 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gardens', '0010_auto_20200609_2124'),
        ('plants', '0004_auto_20200609_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nvm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_garden', models.ForeignKey(on_delete=models.SET(0), to='plants.Plant')),
                ('id_plant', models.ForeignKey(on_delete=models.SET(0), to='gardens.Garden')),
            ],
        ),
    ]
