from django.db import models
# Create your models here.
class Timing(models.Model):
    day = models.CharField(max_length=50, unique=True)
    timing_hours = models.CharField(max_length=100)
