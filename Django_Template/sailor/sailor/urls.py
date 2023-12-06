from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),  
    path('index/', views.index),  
]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('register', views.user_data),
#     path('list', views.user_data),
# ]
