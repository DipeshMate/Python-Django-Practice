from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class loginForm(UserCreationForm):
    class meta:
        model = User
        fields = ['firstname','lastname','email','password']
