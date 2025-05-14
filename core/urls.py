from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Signup routes
    path('signup/patient/', views.patient_signup, name='patient_signup'),
    path('signup/doctor/', views.doctor_signup, name='doctor_signup'),

    # Book appointment (only one route for clarity)
    path('appointment/book/', views.book_appointment, name='book_appointment'),

    # API endpoint for AJAX
    path('api/book_appointment/', views.book_appointment_api,
         name='book_appointment_api'),

    # Video call
    path('video/', views.video_call, name='video_call'),

    # Logout
    path('logout/', LogoutView.as_view(next_page='/home/'), name='logout'),

    # Home page
    path('home/', views.home, name='home'),
]
