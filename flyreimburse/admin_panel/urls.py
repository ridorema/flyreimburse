from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('agency/', views.agency_dashboard, name='agency_dashboard'),
    path('applications/', views.application_list, name='application_list'),
]
