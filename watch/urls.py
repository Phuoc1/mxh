#from mxh.home.views import watch
from django.urls import path
from.import views 
app_name = 'watch'

from .views import watch

urlpatterns = [
#    path('', views.watch, name = 'watch'),
    path('', watch.as_view(),name='watch'),

    path('watchhistory/', views.watchhistory,name='watchhistory'),
]
