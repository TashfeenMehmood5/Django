from django import forms
from .models import DataEntered
class contact(forms.ModelForm):
    class Meta:
        model = DataEntered
        fields = ['User_name','User_email','User_address','User_qualification']
        labels = {'User__name':'Name','User_email':'Email','User_address':'Address','User_qualification':'Education'}
        error_messages = {'User_name':{'required':'Please Enter Your Valid Name'},
        'User_email':{'required':'Please Enter Your email with @'},
        'User_address':{'required':'Please Enter Your Address'},
        'User_qualification':{'required':'Please Enter Your Education'}
        }
        widgets= {
            'User_name':forms.TextInput(attrs={'placeholder':'Enter Your Name'}),
            'User_email':forms.EmailInput(attrs={'placeholder':'example@gmail.com'})
        }