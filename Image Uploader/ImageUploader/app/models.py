from django.db import models

# Create your models here.
class Image(models.Model):
    photos= models.ImageField(upload_to='uploaded_images')
    date_time = models.DateTimeField(auto_now_add=True)
