# Generated by Django 4.2.1 on 2023-06-05 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_organiser_organiser_id_participant_particpant_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organiser',
            name='organiser_id',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='particpant_id',
        ),
    ]
