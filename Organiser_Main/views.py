from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def organiser_main(request, organizer):
    future_events = Organiser_events.objects.filter(organizer=organizer)
    context = {
        'organizer': organizer,
        'events': future_events,
    }
    return render(request, 'org_index.html', context)


def create_event(request, organizer):
    if request.method == 'POST':
        name = request.POST['event_name']
        description = request.POST['event_description']
        date_and_time = request.POST['event_datetime']
        location = request.POST['event_location']
        picture = request.FILES['event_picture']
        max_participants = request.POST['max_participants']

        organiser_instance = Organiser.objects.get(id=organizer)
        
        event = Organiser_events(
            organizer=organiser_instance,
            event_name=name,
            event_description=description,
            event_date=date_and_time,
            event_location=location,
            event_picture=picture,
            event_max_participants=max_participants,
            event_present_participants=0,
        )
        event.save()

        return redirect('organiser_main', organizer=organizer)
    
    return render(request, 'new_org_event.html', {'organizer': organizer})
