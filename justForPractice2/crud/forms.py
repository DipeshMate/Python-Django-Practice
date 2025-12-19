from django import forms
from .models import StudentRegistration

class StudentForm(forms.ModelForm):
    class Meta:
      model = StudentRegistration
      fields = ['name','email','password']
      labels={'name':'Name',
                'email':'Email',
                'password':'Password',
             }
      widgets={'name': forms.TextInput(attrs={'class':'flow-control','placeholder':'Enter your Name'}),
               'email': forms.EmailInput(attrs={'class':'flow-control','placeholder':'Enter your Email'}),
               'password': forms.PasswordInput(render_value=True,attrs={'class':'flow-control','placeholder':'Enter your Password'})
              } 