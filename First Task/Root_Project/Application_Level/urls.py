from django.urls import path
from Application_Level import views
urlpatterns = [
    path("",views.ourhome, name="home"),
]

