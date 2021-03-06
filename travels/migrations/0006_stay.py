# Generated by Django 3.1.3 on 2020-11-28 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0005_auto_20201128_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8, unique=True, verbose_name='Coidgo de Estancia')),
                ('pension', models.CharField(max_length=50, verbose_name='Pension')),
                ('entry_date', models.DateField(verbose_name='Fecha Entrada')),
                ('departure_date', models.DateField(verbose_name='Fecha Salida')),
            ],
            options={
                'verbose_name': 'Estancia',
                'verbose_name_plural': 'Estancias',
            },
        ),
    ]
