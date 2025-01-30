from django.shortcuts import render, redirect
from .models import ClaimSubmission
from django.http import HttpResponse
from .models import ContactMessage, Agency, Application, ClaimSubmission
import requests
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group


def home(request):
    return render(request, 'home.html')




def home(request):
    API_URL = "https://api.aviationstack.com/v1/flights"
    API_KEY = "16c90ae0330f977a33331eec91187224"

    params = {
        'access_key': API_KEY,
        'limit': 20,  # Fetch more flights
        'arr_iata': 'TIA',  # Flights arriving in Tirana (Albania)
        #'dep_iata': 'TIA',  # Uncomment if you also want departing flights
    }

    live_flights = []

    try:
        response = requests.get(API_URL, params=params)
        data = response.json()

        print(data)  # Debug: Check API response in terminal

        if "data" in data:
            for flight in data["data"]:
                if flight.get("live"):  # Include both airborne and upcoming flights
                    live_flights.append({
                        "airline": flight.get("airline", {}).get("name", "Unknown Airline"),
                        "flight_number": flight.get("flight", {}).get("iata", "Unknown"),
                        "departure_airport": flight.get("departure", {}).get("airport", "Unknown Airport"),
                        "departure_iata": flight.get("departure", {}).get("iata", ""),
                        "arrival_airport": flight.get("arrival", {}).get("airport", "Unknown Airport"),
                        "arrival_iata": flight.get("arrival", {}).get("iata", ""),
                        "status": flight.get("status", "Unknown"),
                    })

    except requests.exceptions.RequestException as e:
        print(f"Error fetching flight data: {e}")

    return render(request, 'website/home.html', {'flights': live_flights})


def air_passenger_rights(request):
    return render(request, 'air-passenger-flights.html')

def services(request):
    return render(request, 'website/services.html')

def delayed_compensation_right(request):
    return render(request, 'delayed-compensation-flights.html')

def overbooked_flight(request):
    return render(request, 'overbooked-flight.html')

def cancel_flight(request):
    return render(request, 'cancel-flight.html')

def about(request):
    return render(request, 'about.html')

def form(request):
    return render(request, 'website/form.html')




from .models import ClaimSubmission, Agency

def submit_claim(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        flight_number = request.POST['flight_number']
        date = request.POST['date']
        compensation_amount = request.POST['compensation_amount']

        try:
            agency = Agency.objects.get(user=request.user)  # Ensure agency exists
        except Agency.DoesNotExist:
            messages.error(request, "Error: Your account is not linked to an agency.")
            return redirect('agency_dashboard')

        ClaimSubmission.objects.create(
            agency=agency,  # ✅ Assign the claim to the logged-in agency
            name=name,
            email=email,
            flight_number=flight_number,
            date=date,
            compensation_amount=compensation_amount
        )

        messages.success(request, "Claim submitted successfully!")
        return redirect('agency_dashboard')

    return render(request, 'website/submit_claim.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Mund të shtoni logjikë për të dërguar email ose për të ruajtur në bazën e të dhënave
        return HttpResponse(f'Faleminderit {name}, mesazhi juaj u dërgua me sukses!')
    return render(request, 'website/contact.html')



def send_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the data to the database
        ContactMessage.objects.create(name=name, email=email, message=message)

        return HttpResponse(f'Faleminderit {name}, mesazhi juaj u dërgua me sukses!')
    else:
        return HttpResponse("Kjo faqe nuk është e vlefshme për kërkesat GET.")


def register_agency(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        agency_name = request.POST.get('agency_name')
        contact_email = request.POST.get('contact_email')

        if form.is_valid():
            user = form.save()

            
            agency, created = Agency.objects.get_or_create(user=user, defaults={'agency_name': agency_name, 'contact_email': contact_email})

            
            agency_group, created = Group.objects.get_or_create(name="Agency")
            user.groups.add(agency_group)

            login(request, user)
            return redirect('agency_dashboard')

    else:
        form = UserCreationForm()

    return render(request, 'website/register.html', {'form': form})


@login_required
def dashboard(request):
    agency = Agency.objects.get(user=request.user)
    applications = Application.objects.filter(agency=agency)
    return render(request, 'website/dashboard.html', {'applications': applications})



@login_required
def agency_dashboard(request):
    try:
        # Get the agency linked to the logged-in user
        agency = Agency.objects.get(user=request.user)
        # Fetch claims submitted by this agency
        applications = ClaimSubmission.objects.filter(agency=agency)
    except Agency.DoesNotExist:
        applications = None  # No agency found, so no claims will be shown

    return render(request, 'website/agency_dashboard.html', {'applications': applications})