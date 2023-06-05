from django.contrib import admin
from django.urls import path

from User.views import *
from Organiser_Main.views import *


urlpatterns = [
    path('', Login, name="User_Login"),
    path('signup', Signup, name="User_signup"),
    path('organiser_signup/', Organiser_signup, name='Organiser_signup'),
    path('participant_signup/', Participant_signup, name='Participant_signup'),
    
    path('Organiser',organiser_main,name="organiser_main"),
    
    path('admin/', admin.site.urls),
]