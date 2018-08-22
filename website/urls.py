from django.urls import path
from .views import *

urlpatterns = [
    path('', WelcomeView.as_view()),
    path('event', EventInfoView.as_view(), name='event-info'),
    path('registration/<int:event>', AttendeeRegistrationView.as_view(), name='attendee-registration'),
]
