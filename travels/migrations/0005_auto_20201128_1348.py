# Generated by Django 3.1.3 on 2020-11-28 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0004_tourist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=6, unique=True, verbose_name='Numero de vuelo')),
                ('date', models.DateField(verbose_name='Fecha de vuelo')),
                ('time', models.TimeField(verbose_name='Hora de vuelo')),
                ('origin', models.CharField(max_length=40, verbose_name='Origen')),
                ('destination', models.CharField(max_length=40, verbose_name='Destino')),
                ('total_square', models.PositiveIntegerField(verbose_name='Plaza Total')),
                ('tourist_square', models.PositiveIntegerField(verbose_name='Plaza Turista')),
            ],
            options={
                'verbose_name': 'Vuelo',
                'verbose_name_plural': 'Vuelos',
            },
        ),
        migrations.AlterField(
            model_name='hotel',
            name='square',
            field=models.PositiveIntegerField(verbose_name='Plaza'),
        ),
    ]
