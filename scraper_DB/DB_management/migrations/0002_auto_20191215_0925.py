# Generated by Django 3.0 on 2019-12-15 09:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DB_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightdata',
            name='flight_end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='flightdata',
            name='flight_end_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='flightdata',
            name='flight_st_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='flightdata',
            name='flight_st_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
