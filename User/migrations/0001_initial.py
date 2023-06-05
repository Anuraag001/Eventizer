# Generated by Django 4.2.1 on 2023-06-05 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organiser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('date_of_join', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
