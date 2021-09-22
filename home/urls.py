from django.urls import path
from.import views
app_name ='home'

######################################################



from .views import  SiteRegisterOkView, SiteRegisterView, SiteLogoutView, IndexClass, LoginClass, ViewUser
urlpatterns = [
    #path('',views.index, name = 'home'),
#]




########################################################
########################################################


#urlpatterns = [
#    path('', IndexClass.as_view(), name='index'),

#    path('', ViewUser.as_view(),name='user_view'),
    path('', ViewUser.as_view(),name='home'),

    path('login/', LoginClass.as_view(), name='login'),
    path('user-view/', ViewUser.as_view(),name='user_view'),
    path('logout/',SiteLogoutView.as_view(),name='logout'),
    path('register/',SiteRegisterView.as_view(),name='register'),
    path('ok/',SiteRegisterOkView.as_view(),name='register_ok'),
]
