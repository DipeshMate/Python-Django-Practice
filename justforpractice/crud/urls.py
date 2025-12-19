from django.urls import path
from .views import *
urlpatterns = [
    path('',Home,name='Home'),
    path('studentRegistration/', studentRegistration, name='studentRegistration'),
    path('studentRegistration/<int:id>', delete_Student_Data, name='deleteStudentData'),
    path('updateStudent/<int:id>', updateStudent, name='UpdateStudent'),
    path('updateStudent/', updateStudent, name='UpdateStudent'),
]
