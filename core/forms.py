from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, PatientProfile, DoctorProfile
from .models import Appointment


from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'date_time']



class PatientSignUpForm(UserCreationForm):
    age = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        if commit:
            user.save()
            PatientProfile.objects.create(
                user=user, age=self.cleaned_data['age'])
        return user


class DoctorSignUpForm(UserCreationForm):
    specialization = forms.CharField(max_length=100, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
            DoctorProfile.objects.create(
                user=user, specialization=self.cleaned_data['specialization'])
        return user
