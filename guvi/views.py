from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def HomePage(request):
    return render(request,'index.html')

def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'index.html',{'user':request.user})

def SignupPage(request):
    if request.method=='POST':
        uname= request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your passwords do not match")
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        messages.success(request,'Your account has been created successfully')
        return redirect('login')

    return render (request,'signup.html')




def LoginPage(request):
    if request.method=='POST':
        username= request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse('Incorrect username and password')


    return render (request,'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')

def aboutPage(request):
    return render(request,'about.html')
# Create your views here.
