from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)

class studentAdmin(admin.ModelAdmin):
    list_display=('id','student_name','student_email','student_course','student_progress')
