from django.urls import path
from drf import views
urlpatterns = [
    path('home/',views.Home),
    path('home/<int:id>',views.studentInfo),
    path('stucreate/',views.student_create),
]
