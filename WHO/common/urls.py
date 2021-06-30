from django.contrib import admin
from django.urls import path
from common import views

urlpatterns = [
    path('', views.showHome, name="home_page"),
    path('covid_updates/', views.showCovid, name="covid_page"),
    path('student/', views.showStudent, name="student_page"),
    path('student_otp/', views.showOTP, name="student_otp"),
    path('student_registration/', views.showStudentRegistration, name="student_registration"),
    path('doctor/', views.showDoctor, name="doctor_page"),
    path('admin/', views.showAdmin, name="admin_page"),
    path('contact/', views.showContact, name="contact_page"),
]