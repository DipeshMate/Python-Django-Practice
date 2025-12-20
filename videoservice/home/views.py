from django.shortcuts import render
from .models import *
from datetime import datetime, timedelta
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.



def home(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request , 'home.html' , context)

def view_course(request,slug):
    course = Course.objects.filter(slug =slug).first()
    course_modules = CourseModule.objects.filter(course=course)
    context = {'course':course , 'course_modules':course_modules}
    return render(request, 'course.html' , context)

# @login_required(login_url='/login/')
def become_pro(request):

    return render(request , 'become_pro.html')


def login_attempt(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username).first()
        
        if user is None:
            context = {'message' : 'No user found' , 'class' : 'danger'}
            return render(request,'login.html' , context)
        else:
            user = authenticate(username = username , password = password)
            print(user)
            if user is None:
                context = {'message' : 'Invalid credentials' , 'class' : 'danger'}
                return render(request,'login.html' , context)
            else:
                login(request , user)
                return redirect('home')  

    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username).first()
        if user:
            context = {'message' : 'User already exists' , 'class' : 'danger'}
            return render(request,'register.html' , context)
        else :
            context = {'message' : 'User created successfully' , 'class' : 'success'}
            user = User(username = username)
            user.set_password(password)
            user.save()
            return render(request,'register.html' , context)
        
    return render(request,'register.html')



def logout_attempt(request):
    request.session.profile = None
    logout(request)
    return redirect('/')
        