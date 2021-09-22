from django.urls import path
from .views import  SiteRegisterOkView, SiteRegisterView,  IndexClass, LoginClass, ViewUser #SiteLogoutView,



urlpatterns = [
    path('', IndexClass.as_view(), name='index'),
#    path('login/', LoginClass.as_view(), name='login'),
    path('user-view/', ViewUser.as_view(),name='user_view'),
 #   path('logout/',SiteLogoutView.as_view(),name='logout'),
    path('register',SiteRegisterView.as_view(),name='register'),
    path('register/ok',SiteRegisterOkView.as_view(),name='register_ok'),
]
