from django.shortcuts import render
from .forms import loginForm

# Create your views here.

def login(request):
    return render(request,'login.html',{'form':loginForm})

def signup(request):
    return render(request,'signup.html')
    