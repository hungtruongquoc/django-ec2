# Generated by Django 5.1a1 on 2024-07-12 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_day_roomutilization'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Day',
            new_name='DayPoint',
        ),
    ]
