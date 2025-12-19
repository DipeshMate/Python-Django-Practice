from django.db import models

# Create your models here.

class EmpModel(models.Model):
    gender=(
        ('M','Male'),
        ('F','Female'),
    )
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=1,choices=gender)