from django.urls import path
from autho.views import *

urlpatterns = [
    path('',Home,name='home'),
    path('signup',Sign_Up,name='signup'),
    path('login/',Log_In,name='login'),
    path('logout/',Log_out,name='logout'),
    path('profile/',Profile,name='profile'),
    path('addPost/',AddPost,name='addpost'),
    path('updatePost/<int:id>/',UpdatePost,name='updatepost'),
    path('deletePost/<int:id>/',deletePost,name='deletepost'),
    path('resetpassword/',ResetPassword, name='resetpassword')
]
