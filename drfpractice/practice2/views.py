from django.shortcuts import render
from django.http import HttpResponse
from .models import EmpModel
from .serializer import EmpSerializer
from rest_framework import viewsets

# Create your views here.

class EmpViewSet(viewsets.ModelViewSet):
    queryset = EmpModel.objects.all()
    serializer_class = EmpSerializer
