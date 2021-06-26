from django.contrib import admin
from django.urls import path
from django.urls import include
from common import views

urlpatterns = [
    path('', views.showHome, name='home_page'),
    path('admin/', views.showAdmin, name="admin_page"),
    path('faculty/', views.showFaculty, name="faculty_page"),
    path('student/', views.showStudent, name="student_page"),
    path('contact/', views.showContact, name="contact_page"),

]