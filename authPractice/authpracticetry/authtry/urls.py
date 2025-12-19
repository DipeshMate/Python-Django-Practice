from django.urls import path
from authtry.views import *
urlpatterns = [
    path('login/',login),
    path('',signup),
]
