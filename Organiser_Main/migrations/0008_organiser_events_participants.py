# Generated by Django 4.2.1 on 2023-06-16 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_organiser_contact_participant_contact'),
        ('Organiser_Main', '0007_organiser_events_organizer'),
    ]

    operations = [
        migrations.AddField(
            model_name='organiser_events',
            name='participants',
            field=models.ManyToManyField(blank=True, to='User.participant'),
        ),
    ]