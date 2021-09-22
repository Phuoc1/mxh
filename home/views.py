from django.conf.urls import url
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'home/index.html')
    #return HttpResponse("trang chu")


#####################################################################
#####################################################################

from pprint import pp
from typing import Reversible
from django.forms import widgets
from django.shortcuts import redirect, render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import decorators
# Create your views here.

class IndexClass(View):
    def get(self, request):
        return HttpResponse('<h1>Xin chao</h1>')

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'data-id': 1000}))
    class Meta:
        model = User
        fields = ('username', 'email')
        field_classes = {'username': UsernameField}
        widgets = {
        }

class SiteRegisterView(FormView):
    template_name = 'userlogin/register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        data = form.cleaned_data
        new_user = User.objects.create_user(
            username=data['username'],
            password=data['password1'],
            email=data['email']
        )
        url = f"{reverse('home:register_ok')}?username={new_user.username}"
        return redirect(url)
        #from pprint import pprint; pprint(data)

class SiteRegisterOkView(TemplateView):
    template_name = 'userlogin/register_ok.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.GET.get('usename')
        return context

class LoginClass(View):
    def get(self, request):
        return render(request,'userlogin/login.html')
    def post(self, request):
        tendangnhap = request.POST.get('tendangnhap')
        matkhau = request.POST.get('matkhau')
        my_user = authenticate(username=tendangnhap, password=matkhau) 
        if my_user is None:
        #   return HttpResponse('<h1>Dang nhap thai bai!, User Khong ton tai !!!!!!!!!!!!!!!!!!!!!!!!!</h1>')
            return render(request, 'userlogin/loginsai.html')        
        login(request, my_user)
        #return HttpResponse('<h1>DANG NHAP THANH CONG</h1>')
        return render(request, 'home/index.html')

class ViewUser(LoginRequiredMixin, View): # 
    login_url = '/login/'
    def get(delf, request):
    #    if not request.user.is_authenticated:
    #        return HttpResponse('<h1>Ban vui long dang nhap !!!!!!!!!!!!!!!!!!</h1>')
        #    return render(request, 'userlogin/login.html')
    #    else:
            return render(request, 'home/index.html')

class SiteLogoutView(LogoutView):
    #LoginRequiredMixin, Logout
#    def get(delf, request):
#    template_name = 
#        return render(request, login_url = '/logout.html')


    def get(delf, request):
        return render(request,'userlogin/logout.html')
    def post(self, request):
        tendangnhap = request.POST.get('tendangnhap')
        matkhau = request.POST.get('matkhau')
        my_user = authenticate(username=tendangnhap, password=matkhau) 
        if my_user is None:
            return render(request, 'userlogin/loginsai.html')        
        login(request, my_user)
        return render(request, 'home/index.html')
        


