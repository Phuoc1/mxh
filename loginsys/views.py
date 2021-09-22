from django.shortcuts import render
from django.http import HttpResponse, request
from loginsys.models import Newuser
from django.contrib import messages

# Create your views here.
def loginsys(request):
    return render(request,'loginsys/loginsys.html')

def Userreg(request):
    if request.method=='POST':
        Username=request.POST['Username']
        Email=request.POST['Email']
        Pwd=request.POST['Pwd']
        Age=request.POST['Age']
        Gender=request.POST['Gender']
        Martialstatus=request.POST['Martialstatus']
        Newuser(Username=Username,Email=Email,Pwd=Pwd,Age=Age,Gender=Gender,Martialstatus=Martialstatus).save() 
        messages.success(request,'The New User'+ request.POST['Username'] + "Is Saved Successfully...!")
        return render(request,'loginsys/Registration.html')
    else:
        return render(request, 'loginsys/Registration.html')    



def loginpage(request):
    if request.method=="POST":
        try:
            Userdetails=Newuser.objects.get(Email=request.POST['Email'], Pwd=request.POST['Pwd'])
            print("Username=", Userdetails)
            request.session['Email']=Userdetails.Email
        #    if not request.session['Email']:
        #            return render(request,'loginsys/loginsys.html')
        #    else: 
        #            return render(request,'loginsys/testlogin.html')
            return render(request,'loginsys/loginsys.html')
        #    return render(request,'home/index.html')
        except Newuser.DoesNotExist as e:
            messages.success(request,'Username | Password Invalid...!')    
    return render(request,'loginsys/login.html')
    #return render(request,'home/index.html')



def logout(request):
    try:
        del request.session['Email']
    except:
        return render(request,'loginsys/loginsys.html')
    return render(request,'loginsys/loginsys.html')
 


#def get(request):
#    if not request.session['Email']:
#        return render(request,'loginsys/login.html')
#    else: 
#        return render(request,'loginsys/testlogin.html')