# Generated by Django 4.2.3 on 2023-07-22 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_mileage_alter_car_miles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='passengers',
            field=models.IntegerField(),
        ),
    ]
