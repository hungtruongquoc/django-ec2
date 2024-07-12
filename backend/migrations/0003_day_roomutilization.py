# Generated by Django 5.1a1 on 2024-07-12 21:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_remove_hotel_description_remove_room_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomUtilization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utilization', models.FloatField()),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.day')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.room')),
            ],
            options={
                'unique_together': {('room', 'day')},
            },
        ),
    ]