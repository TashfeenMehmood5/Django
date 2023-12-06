
from django.contrib import admin
from django.urls import path, include
from App import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('about/',views.about, name='aboutus'),
    path('product/',views.product, name='productus'),
    path('store/',views.store, name='storeus'),
    path('simple/',views.simpleForm, name='contactus'),
    path('success/',views.success),
    path('dynamic/<int:id>',views.dynamic, name="dynamic"),
    path('student/',views.student,name="student"),
    path('delete/<int:id>',views.delete ,name="delete"),
    path('edit/<int:id>/',views.update ,name="update"),
    path('signup/',views.reg ,name="signup"),
    path('login/',views.login ,name="login"),
    path('profile/',views.profile ,name="profile"),
    path('logout/',views.logout_profile ,name="logout"),
    path("accounts/", include("allauth.urls")),
    path("security/",views.changepass,name="changepassword"),
     path('edit_profile/', views.edit_profile, name='edit_profile'),
]
