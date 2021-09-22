# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

#################################################

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.



#def watch(request):
#    return render(request,'watch/watch.html')
    

#############################################################
from django.contrib.auth import decorators
from django.views import View

class watch(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(delf, request):
        #if not request.user.is_authenticated:
        #    return HttpResponse('<h1>Ban vui long dang nhap !!!!!!!!!!!!!!!!!!</h1>')
        #    return render(request, 'userlogin/login.html')
        #else:
            return render(request, 'watch/watch.html')


@decorators.login_required(login_url='/login/')    
def watchhistory(request):
    return HttpResponse('Lịch Sử xem')




