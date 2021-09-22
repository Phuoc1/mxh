from django.contrib import admin
from django.urls import path
from django.views.generic.base import View
from.import views


app_name ='loginsys'

urlpatterns = [
    path('',views.loginsys, name ='loginsys'),
    path('Registration',views.Userreg, name="Reg"),
    path('login', views.loginpage,name="Loginpage"),
    path('logout', views.logout,name="Logout"),
    
    path('testlogin/', views.loginpage, name="testlogin" )
]
