from django.shortcuts import render
from Organiser_Main.models import Organiser_events

def participant_main(request, participant):
    events = Organiser_events.objects.all()
    return render(request, 'par_index.html', {'participant': participant, 'events': events})

def participant_event(request, participant, organiser_event):
    event = Organiser_events.objects.get(id=organiser_event)
    is_registered = participant in event.participants.all()
    participants = event.participants.all() 
    if request.method == 'POST':
        if 'unregister' in request.POST:
            event.participants.remove(participant)
            is_registered = False
        else:
            event.participants.add(participant)
            is_registered = True
        
        event.event_present_participants = participants.count()
        event.save()

        return render(request, 'view_event.html', {'participants': participants, 'event': event, 'is_registered': is_registered})

    return render(request, 'view_event.html', {'participants': participants, 'event': event, 'is_registered': is_registered})
