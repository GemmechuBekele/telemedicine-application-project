from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Custom user model
class CustomUser(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)


# Doctor Profile model (linked to CustomUser)
class DoctorProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr. {self.user.username}"


# Patient Profile model (linked to CustomUser)
class PatientProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"Patient {self.user.username}"


# Appointment model
class Appointment(models.Model):
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='appointments_as_doctor'
    )
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='appointments_as_patient'
    )
    date_time = models.DateTimeField()
    status = models.CharField(
        max_length=10,
        choices=[
            ('pending', 'Pending'),
            ('booked', 'Booked'),
            ('completed', 'Completed')
        ],
        default='pending'
    )

    def __str__(self):
        return f"Appointment between Dr. {self.doctor.username} and {self.patient.username} at {self.date_time}"





    



