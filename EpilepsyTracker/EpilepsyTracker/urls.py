
from django.contrib import admin
from django.urls import path
from tracker import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page,name="home"),
    path('about/', views.about_page,name="about"),
    path('contact/', views.contact_page,name="contact"),
    path('dashboard/', views.Dashboard,name="dashboard"),
    path('signup/', views.signup_page,name="signup"),
    path('signin/', views.signin_page,name="signin"),
    path('signout/', views.signout_page,name="signout"),
    
]