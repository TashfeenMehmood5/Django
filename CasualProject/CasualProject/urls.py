from django.contrib import admin
from django.urls import path
from CasualApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about/',views.about, name='aboutus'),
    path('product/',views.product, name='productus'),
    path('store/',views.store, name='storeus'),
    path('simple/',views.simple, name='storeus'),
]
