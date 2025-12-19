from django.shortcuts import render, HttpResponseRedirect
from .models import StudentRegistration
from .forms import StudentForm
# Create your views here.

def Home(request):
    request.session['lname'] = 'Puja'
    return render(request, 'Home.html')

def studentRegistration(request):
    sd = StudentRegistration.objects.all()
    sf = StudentForm(request.POST)
    if request.method == 'POST':
      if sf.is_valid():  
        nm = sf.cleaned_data.get('name')
        em = sf.cleaned_data.get('email')
        pw = sf.cleaned_data.get('password')
        reg = StudentRegistration(name=nm,email=em,password=pw)
        reg.save()
        sf = StudentForm()
    else:
      sf = StudentForm()
    name = request.session.get('lname','Guest')
    return render(request,'Students.html',{'form':sf,'stud':sd,'name':name})

def delete_Student_Data(request,id):
    if request.method == 'POST':
        sd = StudentRegistration.objects.get(pk=id)
        sd.delete()
    return HttpResponseRedirect('/studentRegistration')

def updateStudent(request,id):
    if request.method == 'GET':
        sd = StudentRegistration.objects.get(pk=id)
        sf = StudentForm(instance = sd)
    else:
        sd = StudentRegistration.objects.get(pk=id)
        sf = StudentForm(request.POST, instance = sd)
        if sf.is_valid():  
          sf.save()
        return render(request,'UpdateStudent.html',{'form':sf})
    request.session.flush()
    return render(request,'UpdateStudent.html',{'form':sf})
