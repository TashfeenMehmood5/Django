
from django.contrib import admin
from django.urls import path
from Blog import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page,name="home"),
    path('about/', views.about_page,name="about"),
    path('blog/', views.blog_page,name="blog"),
    path('contact/', views.contact_page,name="contact"),
    path('signup/', views.signup_page,name="signup"),
    path('signin/', views.signin_page,name="signin"),
    path('signout/', views.signout_page,name="signout"),
    path('AddPost/', views.addBlog_page,name="addpost"),
    path('delete/<int:id>',views.delete_page, name='delete'),
    path('update/<int:id>',views.update_page, name='update'),
]