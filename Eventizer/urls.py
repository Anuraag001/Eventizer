from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from User.views import *
from Organiser_Main.views import *
from Participant_Main.views import *

urlpatterns = [
    path('', Login, name='Main'),
    path('User_Login/', Login, name='User_Login'),
    path('Signup/', Signup, name='User_signup'),
    path('organiser_signup/', Organiser_signup, name='Organiser_signup'),
    path('participant_signup/', Participant_signup, name='Participant_signup'),
    path('organiser_signin/', Organiser_signin, name='Organiser_signin'),
    path('organiser_forgot_password/', org_forgot, name='Organiser_forgot_password'),
    path('reset_password/<int:organizer>/', org_reset, name='Organiser_reset'),
    path('participant_signin/', Participant_signin, name='Participant_signin'),
    path('new_event/<int:organizer>/', create_event, name='new_event'),
    path('organiser_main/<int:organizer>/', organiser_main, name='organiser_main'),
    path('organiser_main/<int:organizer>/profile/', organiser_profile, name='organiser_profile'),
    path('Participant/<int:participant>/', participant_main, name='participant_main'),
    path('participant_event/<int:participant>/register/<int:organiser_event>/',participant_event,name='participant_event'),
    path('organiser_event/<int:organiser>/view/<int:organiser_event>/',event_view_org,name='organiser_event_view'),
    path('logout', logout_org, name='logout'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
