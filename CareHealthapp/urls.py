
from django.contrib import admin
from django.urls import path

from CareHealthapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('service/', views.service, name='service-details'),
    path('starter/', views.starter, name='starter-page'),
    path('about/', views.About, name='about'),
    path('services/', views.services, name='services'),
    path('doctors/', views.doctors, name='doctors'),
    path('departments/', views.departments, name='departments'),
    path('contact/', views.contact, name='contact'),
    path('appointment/', views.Appointment, name='appointment'),
]
