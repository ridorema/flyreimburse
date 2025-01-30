from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Agency(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    agency_name = models.CharField(max_length=255, default="Unknown Agency")
    contact_email = models.EmailField(unique=True, default="default@email.com")
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.agency_name

class ClaimSubmission(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, null=True, blank=True)  # ✅ Allows null values
    name = models.CharField(max_length=255)
    email = models.EmailField()
    flight_number = models.CharField(max_length=20)
    date = models.DateField()
    compensation_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')

    def __str__(self):
        return f"{self.name} - {self.flight_number} ({self.status})"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"


#class Agency(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="website_agency")
    #agency_name = models.CharField(max_length=255, default="Unknown Agency")
    #contact_email = models.EmailField(unique=True, default="default@email.com")
    #created_at = models.DateTimeField(default=now) 



class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)  # Agency that owns this application
    passenger_name = models.CharField(max_length=255)
    flight_number = models.CharField(max_length=50)
    date = models.DateField()
    compensation_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.passenger_name} - {self.flight_number}"