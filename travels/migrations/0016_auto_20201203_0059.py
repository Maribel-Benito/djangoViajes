# Generated by Django 3.1.3 on 2020-12-03 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0015_tourist_flight_flight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourist_flight',
            name='flight',
        ),
        migrations.AddField(
            model_name='reserve',
            name='tourist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='travels.tourist', verbose_name='Turista'),
            preserve_default=False,
        ),
    ]
