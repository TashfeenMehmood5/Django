# tracker/admin.py
from django.contrib import admin
from .models import Doctor, Patient,contactTable

@admin.register(Doctor)
class Doctor_Admin(admin.ModelAdmin):
    list_display = ('doctorname','dosage','patientname', 'Schedule', 'start_date', 'end_date', 'time', 'duration', 'severity', 'triggers', 'notes')

@admin.register(Patient)
class Patient_Admin(admin.ModelAdmin):
    list_display = ('id','doctor','doctorname','patientname', 'dosage', 'Schedule', 'start_date', 'end_date')

@admin.register(contactTable)
class ContactTable_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phoneno', 'message')



