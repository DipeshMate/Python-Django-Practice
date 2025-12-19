from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.models import User


#password - dmate@@@##$$$
# Create your views here.

def index(request):
    print(request.user)
    if request.user.is_anonymous:
       return redirect("/login")
    return render(request,'logout.html')

def loginUser(request):
    if request.method == 'POST':
        userw = request.POST.get('username')
        passw = request.POST.get('password')
        print(userw, passw)
        user = authenticate(username=userw, password=passw)
    
        if user is not None:
           messages.success(request, "Login Succesfully.")
           login(request, user)
           return redirect('/')
        else:
           messages.warning(request, "Please Enter Valid Username & Password!!")
           return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    messages.success(request, "Logged Out Successfully.")
    return redirect('/login')