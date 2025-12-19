from django.db import models

# Create your models here.

class StudentDetail(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)