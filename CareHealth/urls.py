
from django.contrib import admin
from django.urls import path,include
from CareHealthapp import views

urlpatterns = [
    path('', include('CareHealthapp.urls')),
]
