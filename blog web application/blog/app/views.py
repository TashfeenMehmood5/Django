from django.shortcuts import render ,redirect
from .forms import contact
from .models import DataEntered
from django.contrib import messages

# Create your views here.
def home(request):
    n1 = "Welcome to  Django"
    n2 = "Home Page"
    n3 = """Every cup of our quality artisan coffee starts with locally sourced, 
    hand picked ingredients. Once you try it, our coffee will be a blissful addition 
    to your everyday morning routine - we guarantee it!"""
    n4 = "Visits today!"
    d = {'n1':n1,'n2':n2,'n3':n3,'n4':n4}
    return render(request,'index.html',d)
def about(request):
    n1 = "Welcome to About Section"
    n2 = "Django About"
    n3 = """Founded in 1987 by the Hernandez brothers, our establishment has been serving up rich coffee sourced from artisan farmers in various regions of South and Central America. We are dedicated to travelling the world, 
    finding the best coffee, and bringing back to you here in our cafe.
    We guarantee that you will fall in lust with our decadent blends the moment you walk inside until you finish your last sip. Join us for your daily routine, an outing with friends, or simply just to enjoy some alone time."""
    d = {'n1':n1,'n2':n2,'n3':n3}
    return render(request,'about.html',d)

def contact(request):
    return render(request,'contact.html')

def simpleForm(request):
    if request.method =='POST':
        form = contact(request.POST)
        if form.is_valid():
            name = form.cleaned_data['User_name']
            email = form.cleaned_data['User_email']
            address = form.cleaned_data['User_address']
            qualification = form.cleaned_data['User_qualification'] 
            s = DataEntered(User_name=name,User_email=email,User_address=address,User_qualification=qualification)
            s.save()
            messages.add_message(request,messages.SUCCESS,"Thank You, your data has been submitted")
            # return render(request,'success.html',{'name':name})
    else:
        form = contact(auto_id=True)
    data_entry = DataEntered.objects.all()
    return redirect(request,'Simpleform.html',{'form':form,'D':data_entry})


        