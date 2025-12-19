from django.shortcuts import render, HttpResponseRedirect
from .models import StudentRegistration
from .forms import StudentForm
from django.views.generic.base import View, TemplateView, RedirectView


# class Home(View):
#     def get (self,request):
#         return render(request,'Home.html')

# class Home(TemplateView):
#     template_name = 'Home.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['name'] = 'Raj'
#         context['title'] = 'Malhotra'
#         print(context)
#         print('key word args like id:',kwargs)
#         return context

# class Homies(RedirectView):
#     pattern_name='mhomies'
    
#     permanent= True
#     query_string= True
      
#     def get_redirect_url(self, *args, **kwargs):
#         print(kwargs)
#         kwargs['id'] = 777
#         return super().get_redirect_url(*args, **kwargs)
    
    

class studentRegistration(TemplateView):
    template_name=''
    def post(self,request):
        sf = StudentForm(request.POST)
        if request.method == 'POST':
            if sf.is_valid():  
                nm = sf.cleaned_data.get('name')
                em = sf.cleaned_data.get('email')
                pw = sf.cleaned_data.get('password')
                reg = StudentRegistration(name=nm,email=em,password=pw)
                reg.save()
                sf = StudentForm()
                return HttpResponseRedirect('/studentRegistration/')
             
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sd = StudentRegistration.objects.all()
        sf = StudentForm()
        context = {'form':sf,'stud':sd}
        return context

class delete_Student_Data(RedirectView):
    url='/studentRegistration/'
    def get_redirect_url(self, *args, **kwargs):
        sd = StudentRegistration.objects.get(pk=kwargs['id'])
        sd.delete()
        return super().get_redirect_url(*args, **kwargs)

class updateStudent(TemplateView):
    template_name=''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sd = StudentRegistration.objects.get(pk=kwargs['id'])
        sf = StudentForm(instance = sd)
        context = {'form':sf}
        return context
    
    def post(self,request,id):
        sd = StudentRegistration.objects.get(pk=id)
        sf = StudentForm(request.POST, instance = sd)
        if sf.is_valid():  
          sf.save()
        return render(request, self.template_name,{'form':sf})
