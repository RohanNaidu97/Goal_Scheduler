"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from pages.views import home_view,dashboard_view,about_view

from django.urls import include

urlpatterns = [
    path('', home_view, name='home'),
    path('about/',about_view, name='about'),
    path('dashboard/',dashboard_view),
    path('admin/', admin.site.urls, name='login'),
    #path('test/',home_view, name='home'),
   
    #BOOKS APP
    path('books/', include('books.urls')),

    #NEW APP MONTHLY_GOALS STARTS HERE
     path('Monthlygoals/', include('Monthlygoals.urls')),

    #NEW APP SCHEDULE STARTS HERE
    path('Schedule/', include('Schedule.urls')),

    #DOLIST APP
    path('Dolist/', include('Dolist.urls')),
]
