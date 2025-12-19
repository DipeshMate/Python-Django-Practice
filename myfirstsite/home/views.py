from django.shortcuts import render, HttpResponse
from django.contrib import messages
from datetime import datetime
from home.models import Contact
from django.views.generic.base import TemplateView, View
from django.template import Template
from .forms import CourseForm

# type 1 - base class view

# class course(View):
#     name= 'Raj'
#     def get(self,request):
#         return HttpResponse(f'<H2>This is List of {self.name} Course</H2>')
    
# class course2(course):
#     def get(self,request):
#         return HttpResponse(f'<H2>This is List of {self.name} Course2</H2>')

# type 2 - base class view

# def course(request):
#     if request.method == 'POST':
#         fm = CourseForm(request.POST)
#         if fm.is_valid():
#            nm = fm.cleaned_data['name']
#            print(nm)
#            return render(request,'course.html',{'form':fm,'name':nm})
#     else:
#         fm = CourseForm()
#     return render(request,'course.html',{'form':fm})

class course(View):
    template_name = 'course.html'
    def get(self, request):
        fm = CourseForm()
        return HttpResponse(request,'adsl')
    def post(self, request):
        fm = CourseForm(request.POST)
        if fm.is_valid():
           nm = fm.cleaned_data['name']
           print(nm)
           return render(request, self.template_name,{'form':fm,'name':nm})
             

# type 2 - Template class view

class course2(TemplateView):
    template_name = 'course.html'


def index(request):
    return render(request, 'home.html')

def about(request):
    context={
        "vari":"About Page:"
    }
    return render(request,'about.html',context)

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        
        #creating Contact object
        contact=Contact(name=name,email=email,phone=phone,desc=desc, date=datetime.today()) 
        
        # Save to database
        contact.save()
        messages.success(request, 'Submitted successfully!')
    return render(request,'contact.html')

def services(request):
    context={
        'justVariable':'Just Services:'
    }
    return render(request,'services.html',context)
