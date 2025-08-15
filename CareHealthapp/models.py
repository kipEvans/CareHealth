from django.db import models

# Create your models here.
class patient(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.firstname +""+ self.surname

class Ward(models.Model):
    wardname = models.CharField(max_length=100)
    capacity = models.IntegerField()
    department = models.CharField(max_length=100)
    descryption = models.TextField()
    staff = models.IntegerField()

    def __str__(self):
        return self.wardname

class Doctor(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    speciality = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    maritalStatus = models.CharField(max_length=100)
    appointmenttime = models.DateTimeField()
    message = models.TextField()

    def __str__(self):
        return self.fullname

class Appoint(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    date = models.DateTimeField()
    department = models.CharField(max_length=100)
    doctor = models.CharField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    mwssage = models.TextField()

    def __str__(self):
        return self.name
