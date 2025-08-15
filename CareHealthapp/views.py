from django.shortcuts import render,redirect
from CareHealthapp.models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def service(request):
    return render(request,'service-details.html')

def starter(request):
    return render(request,'starter-page.html')

def About(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def doctors(request):
    return render(request, 'doctors.html')

def departments(request):
    return render(request, 'departments.html')

def contact(request):
    return render(request, 'contact.html')

def Appointment(request):
    if request.method == 'POST':
        myappointment = Appoint(
            name=request.POST["name"],
            email=request.POST["email"],
            phone=request.POST["phone"],
            date=request.POST["date"],
            department=request.POST["department"],
            doctor=request.POST["doctor"],
            message=request.POST["message"],
        )

        myappointment.save()
        return redirect('/')

    else:
        return render(request, 'appointment.html')