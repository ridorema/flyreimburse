from django.contrib.auth.views import LoginView, LogoutView

from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_claim, name='submit_claim'),
    path('air-passenger-rights/', views.air_passenger_rights, name='air_passenger_rights'),
    path('delayed-compensation-right/', views.delayed_compensation_right, name='delayed_compensation_right'),
    path('overbooked-flight/', views.overbooked_flight, name='overbooked_flight'),
    path('cancel-flight/', views.cancel_flight, name='cancel_flight'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    path('contact/', views.contact, name='contact'),
    path('send-message/', views.send_message, name='send_message'),
    path('register/', views.register_agency, name='register_agency'),
    #path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/', views.agency_dashboard, name='website/agency_dashboard.html'),  # New custom dashboard
    path('login/', LoginView.as_view(template_name='website/login.html'), name='login'),  # Add this
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('services/', views.services, name='services')
    
]
