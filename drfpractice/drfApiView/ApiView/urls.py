from django.urls import path
from ApiView import views

urlpatterns = [
    path('Home/',views.Home),
]
