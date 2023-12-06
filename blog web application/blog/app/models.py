
from django.db import models

class DataEntered(models.Model):
    User_name=models.CharField(max_length=50)
    User_email=models.EmailField(max_length=254)
    User_address=models.CharField(max_length=50)
    User_qualification =models.TextField()
