from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def organiser_main(request):
    future_events = Organiser_events.objects.all()
    return render(request, 'org_index.html', {'events': future_events})

def create_event(request):
    if request.method == 'POST':
        name = request.POST['event_name']
        description = request.POST['event_description']
        date_and_time = request.POST['event_datetime']
        location = request.POST['event_location']
        picture = request.FILES['event_picture']
        max_participants = request.POST['max_participants']

        event = Organiser_events(
            event_name=name,
            event_description=description,
            event_date=date_and_time,
            event_location=location,
            event_picture=picture,
            event_max_participants=max_participants,
            event_present_participants=0,
        )
        event.save()

        # Redirect to the organiser_main view to display the updated list of events
        return redirect('organiser_main')

    return render(request, 'new_org_event.html')