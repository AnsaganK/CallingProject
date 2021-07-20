from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('patients', views.patients_list, name='patients_list'),
    path('managers', views.managers_list, name='managers_list'),
    path('about', views.about_service, name='about_service'),
    path('contacts', views.contacts, name='contacts'),
]