from django.db import models
from django.contrib.auth.models import User


class Agency(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="admin_panel_agency")
    agency_name = models.CharField(max_length=255, default="Unknown Agency")
    contact_email = models.EmailField(unique=True, default="default@email.com")
    created_at = models.DateTimeField(auto_now_add=True)



class Application(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name="applications")
    claim_submission = models.ForeignKey('website.ClaimSubmission', on_delete=models.CASCADE)
    date_submitted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="Pending")  # e.g., Pending, Approved, Rejected

    def __str__(self):
        return f"{self.agency.name} - {self.claim_submission.flight_number}"
