# Generated by Django 3.1.3 on 2020-11-28 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0008_reserve'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reserve',
            options={'verbose_name': 'Reserva', 'verbose_name_plural': 'Reservas'},
        ),
    ]