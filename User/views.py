from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from .models import *
from Organiser_Main.models import *

def Login(request):
    return render(request, 'login.html')

def Signup(request):
    return render(request, 'signup.html')

def Organiser_signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name_org']
        last_name = request.POST['last_name_org']
        email = request.POST['email_org']
        password = request.POST['password_org']
        confirm_password = request.POST['confirmpassword_org']
        profile_picture = request.FILES.get('profile_picture_org')

        if password == confirm_password:
            organiser = Organiser(
                first_name=first_name,
                last_name=last_name,
                email_id=email,
                password=password,
                profile_picture=profile_picture,
            )
            organiser.save()
            return render(request, 'org_index.html',{'app_name':'Organiser_Main'})

        return render(request, 'signup_organiser.html')

    return render(request, 'signup_organiser.html')

def Organiser_signin(request):
    if request.method == 'POST':
        email = request.POST.get('email_org')
        password = request.POST.get('password_org')
        try:
            organiser = Organiser.objects.get(email_id=email)
            
            if password == organiser.password:
                # Password is correct
                return redirect('organiser_main', organizer=organiser.id)  # Include the organizer parameter
            else:
                # Invalid password
                return render(request, 'login.html', {'error_message': 'Invalid email or password'})
        except Organiser.DoesNotExist:
            # Organiser with the given email doesn't exist
            return render(request, 'login.html', {'error_message': 'Invalid email or password'})

    return render(request, 'login.html')


def Participant_signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name_par']
        last_name = request.POST['last_name_par']
        email = request.POST['email_par']
        password = request.POST['password_par']
        confirm_password = request.POST['confirmpassword_par']
        profile_picture = request.FILES.get('profile_picture_par')

        if password == confirm_password:
            participant= Participant(
                first_name=first_name,
                last_name=last_name,
                email_id=email,
                password=password,
                profile_picture=profile_picture,
            )
            participant.save()
            events=Organiser_events.objects.all()
            return render(request, 'par_index.html',{'app_name':'Participant_Main','events':events})

        return render(request, 'signup_participant.html')

    return render(request, 'signup_participant.html')

def Participant_signin(request):
    events=Organiser_events.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email_par')
        password = request.POST.get('password_par')
        try:
            participant = Participant.objects.get(email_id=email)
            
            if password==participant.password:
            # Password is correct
                return render(request, 'par_index.html', {'app_name': 'Participant_Main','events':events})
            else:
            # Invalid password
                return render(request, 'login.html', {'error_message': 'Invalid email or password'})
        except Participant.DoesNotExist:
        # Organiser with the given email doesn't exist
            return render(request, 'login.html', {'error_message': 'Invalid email or password'})

    return render(request, 'login.html')