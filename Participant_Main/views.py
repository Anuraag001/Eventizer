from django.shortcuts import render
from django.http import HttpResponse
from Organiser_Main.models import *

def participant_main(request, participant):
    events = Organiser_events.objects.all()
    return render(request, 'par_index.html', {'participant': participant, 'events': events})

def participant_event(request, participant, organiser_event):
    events=Organiser_events.objects.get(id=organiser_event)
    return render(request, 'view_event.html', {'participant': participant, 'event': events})
