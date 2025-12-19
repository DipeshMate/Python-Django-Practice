from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about),
    path("contact",views.contact),
    path("services",views.services),
    # path('course',views.course),
    path('course',views.course.as_view(),name='course'),
    #path('course',views.course.as_view(name='sonam')),
   # path('course2',views.course2.as_view()),
    
]