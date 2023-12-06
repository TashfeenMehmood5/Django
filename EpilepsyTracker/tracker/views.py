from django.shortcuts import render, redirect,HttpResponseRedirect
from tracker.forms import contact, sigupForm, signin , Doctor_Admin_Form, Patient_user_Form
from tracker.models import contactTable
from django.contrib import messages 
from django.contrib.auth.models import Group,User
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, update_session_auth_hash, login

def home_page(request):
    return render(request,'index.html')

def about_page(request):
    return render(request,'about.html')

def contact_page(request):
    if request.method =='POST':
        form = contact(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phoneno = form.cleaned_data['phoneno']
            message = form.cleaned_data['message']
            CT = contactTable(name=name,email=email,phoneno=phoneno,message=message)
            CT.save()
            messages.add_message(request,messages.SUCCESS,"Thank You For Contacting Us, we will get back soon!")
    else:
        form = contact(auto_id=True)
    return render(request,'contact.html',{'form':form})

def signup_page(request):
    if request.method == "POST":
        form =  sigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            get = Group.objects.get(name='Editor')
            user.groups.add(get)
            messages.add_message(request,messages.SUCCESS,"Congratulations Your Account Has Been CreatedSuccessfully!")
    else:
        
        form =  sigupForm()
    return render(request,'signup.html',{'form':form})


def signin_page(request):
    if not request.user.is_authenticated:
        if request.method == "POST": 
            form = signin(request=request.user,data=request.POST)
            if form.is_valid():
                username = request.POST["username"]
                password = request.POST["password"]
                user = authenticate(request, username=username, password=password)
                if user is not None:
                        login(request, user) 
                        return redirect('/profile/')
            else:
              return redirect('/signin/')
    else:
        return render(request,'signin.html',{'form':form})

def Dashboard(request):
  if request.user.is_authenticated:
      if request.method == "POST":
        if request.user.is_superuser == True:
          fm = Doctor_Admin_Form(request.POST, instance = request.user)
          users = User.objects.all()  
        else:
          fm = Patient_user_Form(request.POST, instance = request.user)
        if fm.is_valid():
            messages.success(request, "Patients Record is Updated !")
            fm.save()
        else:
            if request.user.is_superuser == True:
                users = User.objects.all()
                fm = Doctor_Admin_Form(instance = request.user)
            else:
                fm = Patient_user_Form(instance = request.user)
        return render(request, 'profile.html', {'name': request.user,'form':fm,'users':users})
   
  else:
       return HttpResponseRedirect('/signin/')
            
def signout_page(request):
    logout(request)
    return redirect('/signin/')
                    
