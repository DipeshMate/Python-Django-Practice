from django.urls import path
from userprofile import views


urlpatterns = [
    path("",views.index,name='userprofile'),
    path("login",views.loginUser,name='login'),
    path("logout",views.logoutUser,name='logout'),   
]
