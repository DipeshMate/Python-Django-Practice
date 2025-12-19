from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from .models import Post

class SignUp_Form(UserCreationForm):
    email = forms.EmailField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }
        
class Login_Form(AuthenticationForm):
    email = forms.EmailField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    username = UsernameField(label='Username',widget=forms.TextInput(attrs={'autofocus': True ,'class':'form-control'}))
    password = forms.CharField(label='Password', 
                               widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    class Meta:
        model = User
        fields = ['email']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','desc']
        labels = {'title':'Title', 'desc':'Description'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
                    'desc':forms.Textarea(attrs={'class':'form-control'}),
                    }