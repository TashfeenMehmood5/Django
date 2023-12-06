# tracker/models.py
from django.db import models

class contactTable(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phoneno = models.IntegerField()
    message = models.TextField()

class Doctor(models.Model):
    doctorname = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    hospital = models.CharField(max_length=200)
    license_number = models.CharField(max_length=50)
    patientname = models.TextField()
    dosage = models.CharField(max_length=50)
    Schedule = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    time = models.TimeField()
    duration = models.DurationField()
    severity = models.CharField(max_length=100)
    triggers = models.TextField()
    notes = models.TextField()

class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    doctorname = models.CharField(max_length=100)
    patientname = models.TextField()
    dosage = models.CharField(max_length=50)
    Schedule = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    

   



