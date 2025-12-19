from django.urls import path,include
from rest_framework.routers import DefaultRouter
from practice2 import views

# creating Router Object
router = DefaultRouter()

#Register EmpViewSet with Router
router.register(r'EmpViewSet',views.EmpViewSet,basename='Employee')

urlpatterns = [
    path('index/',include(router.urls)),
]
