from django.db import models
from User.models import Organiser
# Create your models here.
class Organiser_events(models.Model):
    organizer = models.ForeignKey(Organiser, on_delete=models.CASCADE,default=1)
    event_name = models.CharField(max_length=100)
    event_description = models.CharField(max_length=500)
    event_date = models.DateTimeField()
    event_location = models.CharField(max_length=50)
    event_picture = models.ImageField(upload_to='event_images/')
    event_max_participants = models.IntegerField()
    event_present_participants = models.IntegerField(default=0)