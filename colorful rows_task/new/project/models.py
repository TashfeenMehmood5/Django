from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=50)
    student_email=models.EmailField(max_length=254)
    student_course=models.CharField(max_length=50)
    student_progress=models.TextField()