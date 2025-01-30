from django.contrib import admin
from .models import ContactMessage
from .models import Agency, Application
from .models import ClaimSubmission

@admin.register(ClaimSubmission)
class ClaimSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'flight_number', 'date', 'compensation_amount', 'status', 'agency')
    list_filter = ('status', 'date')
    search_fields = ('name', 'flight_number', 'agency__agency_name')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # Columns to display in the admin list view
    search_fields = ('name', 'email', 'message')   # Search functionality
    list_filter = ('created_at',)                 # Filter by date

@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ('agency_name', 'contact_email', 'created_at')
    search_fields = ('agency_name', 'contact_email')
    list_filter = ('created_at',)
    

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('passenger_name', 'flight_number', 'date', 'compensation_amount', 'status', 'agency')
    list_filter = ('status', 'date')
    search_fields = ('passenger_name', 'flight_number', 'agency__agency_name')

    def get_queryset(self, request):
        """ Agencies can only see their own applications """
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            agency = Agency.objects.get(user=request.user)
            return queryset.filter(agency=agency)
        return queryset
