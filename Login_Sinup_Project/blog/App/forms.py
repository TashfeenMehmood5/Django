
from django import forms
from .models import DataEntered
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
class contact(forms.ModelForm):
    class Meta:
        model = DataEntered
        fields = ['User_name','User_email','User_address','User_qualification']
        labels = {'User_name':'Name','User_email':'Email','User_address':'address','User_qualification':'Education'}
        error_messages = {'User_name':{'required':'Please Enter Your Valid Name'},
        'User_email':{'required':'Please Enter Your email with @'},
        'User_address':{'required':'Please Enter Your Course Name'}
        }
        widgets= {
            'User_name':forms.TextInput(attrs={'placeholder':'Enter Your Name'}),
            'User_email':forms.EmailInput(attrs={'placeholder':'example@gmail.com'})
        }
        
class customregistration(UserCreationForm):
    password1=forms.CharField(min_length=8, max_length=60,widget=forms.PasswordInput(attrs={'class':'form-control','id':'password1'}),label="Password")
    password2=forms.CharField(min_length=8, max_length=60,widget=forms.PasswordInput(attrs={'class':'form-control','id':'password2'}),label="Confirm Password") 

    class Meta:
        model = User
        fields = ['username','email']
        widgets= {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            # 'first_name':forms.TextInput(attrs={'class':'form-control'}),
            # 'last_name':forms.TextInput(attrs={'class':'form-control'}),
        }




