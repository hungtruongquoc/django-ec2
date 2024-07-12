# Generated by Django 5.1a1 on 2024-07-12 21:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='room',
            name='description',
        ),
        migrations.AddField(
            model_name='hotel',
            name='address',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.hotel'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]