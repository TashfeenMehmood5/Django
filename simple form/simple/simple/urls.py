
from django.contrib import admin
from django.urls import path
from form import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about/',views.about, name='aboutus'),
    path('product/',views.product, name='productus'),
    path('store/',views.store, name='storeus'),
    path('contact/',views.contact, name='contactus'),
    path('simpleForm/',views.simpleForm, name='simpleform'),
    path('store/',views.simple, name='simple'),
]
