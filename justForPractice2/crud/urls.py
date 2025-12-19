from django.urls import path
from crud import views
urlpatterns = [
    
    # path('',views.Home.as_view(),name='Home'),
    
    #-------------------------------------------------------------------------------------------------------------------------------#
    #  path('',views.TemplateView.as_view(template_name='Home.html', extra_context={'name':'Raj','title':'Malhotra','age':23}),name='Home'), # no need to define its class
    #  path('home/<int:id>/',views.TemplateView.as_view(template_name='Home.html', extra_context={'name':'Raj','title':'Malhotra','age':23}),name='Home'), # no need to define class kwargs for primary key
    #  path('',views.Home.as_view(extra_context={'age':23}),name='Home'), # with class
    #  path('home/<int:id>/',views.Home.as_view(extra_context={'age':23}),name='Home'), # with class
    #-------------------------------------------------------------------------------------------------------------------------------#
    
    path('',views.TemplateView.as_view(template_name='Home.html'),name='blankhome'),
    # path('index/',views.RedirectView.as_view(url='/'),name='index'), #redirect without child class
    # path('index/',views.RedirectView.as_view(pattern_name='blankhome'),name='index'), #redirect without child class
    # path('homie/',views.RedirectView.as_view(pattern_name='blankhome'),name='homie'), #redirect without child class
    # path('homie/<int:id>/',views.Homies.as_view(),name='homies'), # redirect with child class
    # path('/<int:id>/',views.TemplateView.as_view(template_name='Home.html',extra_context={'name':'name'}),name='mhomies'), # redirect with child class
    # path('site/',views.RedirectView.as_view(url='https://www.linkedin.com/in/dipeshmate/'),name='index'), #redirect to external site with child redirectview class
    #-------------------------------------------------------------------------------------------------------------------------------#
    path('studentRegistration/', views.studentRegistration.as_view(template_name='Students.html'), name='studentRegistration'),
    path('studentRegistration/<int:id>', views.delete_Student_Data.as_view(), name='deleteStudentData'),
    path('updateStudent/<int:id>', views.updateStudent.as_view(template_name='UpdateStudent.html'), name='UpdateStudent'),
    path('updateStudent/', views.updateStudent.as_view(template_name='Students.html'), name='UpdateStudent'),
]
