"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include

from users import views  as user_views
from django.contrib.auth import views as authentication_views

from portfolio import views

from django.conf.urls.static import static   # to click and view the image uploaded in django admin


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings       # to access information from the settings.py file

urlpatterns = [
    path('admin/', admin.site.urls),

    path('' , include('portfolio.urls') ),

    path('project/', include('project.urls')) ,

    path('register/', user_views.register , name ='register'),

    path('login/' , authentication_views.LoginView.as_view(template_name ='users/login.html') , name ='login') ,
    # above url will use an inbuilt view  (authentication_views )  above is a class based view, need to have .as_view()

    path('logout/', authentication_views.LogoutView.as_view(template_name ='users/logout.html'), name='logout') ,
    # these two views  loginview and logoutview are already created by django.  now we to build templates for these

    path('profile/' , user_views.profilepage  , name ='profile') ,

]


#urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
# necessary when working with static files

