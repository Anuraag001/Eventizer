from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Organiser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    contact = models.IntegerField(validators=[MaxValueValidator(9999999999)],default=0)
    profile_picture = models.ImageField(upload_to='profile_pictures_organiser/', null=True, blank=True)
    date_of_join = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Participant(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    contact = models.IntegerField(validators=[MaxValueValidator(9999999999)],default=0)
    profile_picture = models.ImageField(upload_to='profile_pictures_participant/', null=True, blank=True)
    date_of_join = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
