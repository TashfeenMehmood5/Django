from django.contrib import admin
from .models import DataEntered
@admin.register(DataEntered)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','User_name','User_email','User_address','User_qualification')