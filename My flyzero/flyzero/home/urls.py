
from django.urls import path,include
from .views import *

urlpatterns = [

    path('' , home , name="home"),
    path('subject/<slug>' ,view_subject , name="subject"),
    path('become_pro/' , become_pro , name="become_pro"),
    path('charge/' , charge , name="charge"),
    path('login/'  , login_attempt , name="login"),
    path('register/'  , register , name="register"),
    path('logout_attempt/' , logout_attempt , name="logout")
    
  
]