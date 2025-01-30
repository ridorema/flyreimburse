from django.shortcuts import render
from .models import Agency, Application

def dashboard(request):
    # Admin dashboard view
    return render(request, 'admin_panel/dashboard.html')

def agency_dashboard(request):
    # View for agencies to manage applications
    return render(request, 'admin_panel/agency_dashboard.html')

def application_list(request):
    # Admin view to list and manage all applications
    return render(request, 'admin_panel/application_list.html')
