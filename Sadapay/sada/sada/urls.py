
from django.contrib import admin
from django.urls import path
from pay import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.heading),
    path('about/',views.about),
]
