from django.shortcuts import render
from django.http import HttpResponse
from .models import *

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

        return render(request, 'signup.html')

    return render(request, 'signup.html')

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
            return render(request, 'par_index.html',{'app_name':'Participant_Main'})

        return render(request, 'signup.html')

    return render(request, 'signup.html')
