from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.utils import timezone
from .models import *
from .models import Organiser_events


# Create your views here.
def organiser_main(request, organizer):
    future_events = Organiser_events.objects.filter(organizer=organizer, event_date__gte=timezone.now())
    past_events = Organiser_events.objects.filter(organizer=organizer, event_date__lt=timezone.now())
    context = {
        'organizer': organizer,
        'events': future_events,
        'past_events':past_events,
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

def event_view_org(request,organiser,organiser_event):
    event = Organiser_events.objects.get(id=organiser_event)
    participants=event.participants.all()
    if request.method=='POST':
        participant_id=request.POST.get('Participant_id')
        participant = event.participants.get(id=participant_id)
        event.participants.remove(participant)
        event.event_present_participants = participants.count()
        event.save()
    return render(request,'event_view.html',{'event':event,'organiser':organiser,'participants':participants})

def logout_org(request):
    logout(request)
    return render(request, 'login.html')

def organiser_profile(request,organizer):
    return render(request,'org_profile.html',{'organizer':organizer})
