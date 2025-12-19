from django.db import models

class StudentDetail(models.Model):
    name = models.CharField(max_length=50)
    roll = models.CharField(max_length=10)
    age = models.IntegerField()
    
    def __str__(self):
        return f'{self.name}'