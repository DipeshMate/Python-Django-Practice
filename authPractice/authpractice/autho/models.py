from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000)
    
    def __str__(self):
        return f'{self.title}'

