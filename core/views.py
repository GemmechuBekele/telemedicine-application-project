from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, DoctorProfile, PatientProfile, Appointment
from .forms import PatientSignUpForm, DoctorSignUpForm, AppointmentForm

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@csrf_exempt
def book_appointment_api(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        time = request.POST.get('time')
        if not time:
            return JsonResponse({'error': 'Missing time'}, status=400)

        # Get first available doctor
        doctor = DoctorProfile.objects.first()
        if not doctor:
            return JsonResponse({'error': 'No doctor available'}, status=400)

        # Create appointment
        Appointment.objects.create(
            patient=request.user,
            doctor=doctor,
            time=time
        )

        return JsonResponse({'message': 'Appointment booked successfully!'})

    return JsonResponse({'error': 'Invalid request'}, status=400)


def home(request):
    doctors = DoctorProfile.objects.all()
    return render(request, 'core/home.html', {'doctors': doctors})


def dashboard(request):
    return render(request, 'core/dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('dashboard')


def video_call(request):
    return render(request, 'core/video_call.html')


def patient_signup(request):
    if request.method == "POST":
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_patient = True
            user.save()
            PatientProfile.objects.create(user=user)
            login(request, user)
            return redirect('dashboard')
    else:
        form = PatientSignUpForm()
    return render(request, 'core/patient_signup.html', {'form': form})


def doctor_signup(request):
    if request.method == "POST":
        form = DoctorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_doctor = True
            user.save()
            DoctorProfile.objects.create(user=user)
            login(request, user)
            return redirect('dashboard')
    else:
        form = DoctorSignUpForm()
    return render(request, 'core/doctor_signup.html', {'form': form})


# Optional: keep this only if you're using the non-AJAX form
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Or another success page
    else:
        form = AppointmentForm()

    return render(request, 'core/book_appointment.html', {'form': form})
