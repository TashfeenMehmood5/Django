from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about/',views.about, name='aboutus'),
    path('product/',views.product, name='productus'),
    path('store/',views.store, name='storeus'),
    path('simple/',views.simpleForm, name='contactus'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>',views.update, name='update'),
]