from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from User.views import *
from Organiser_Main.views import *
from Participant_Main.views import *

urlpatterns = [
    path('', Login, name="User_Login"),
    path('Signup', Signup, name="User_signup"),
    path('organiser_signup/', Organiser_signup, name='Organiser_signup'),
    path('participant_signup/', Participant_signup, name='Participant_signup'),
    path('organiser_signin/', Organiser_signin, name='Organiser_signin'),
    path('participant_signin/', Participant_signin, name='Participant_signin'),
    path('Organiser',organiser_main,name="organiser_main"),
    path('Participant',participant_main,name="participant_main"),
    path('admin/', admin.site.urls),
    path('new_event',create_event,name="new_event"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
