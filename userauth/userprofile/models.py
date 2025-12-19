# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# admin - mate/developer.mate@gmail.com.
# pass - same321.

# Django Custom User Model

class MyAccountManager(BaseUserManager):
    def create_user(self,email,username, first_name, last_name, phone_number, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')
        
        if not phone_number:
            raise ValueError('User Must have an phone number')
        
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username, first_name, last_name,phone_number, password):
        user = self.create_user(
            username = username,
            email = self.normalize_email(email),
            password = password,
            first_name = first_name,
            last_name = last_name,
            phone_number=phone_number,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Custom User account model 
class Account(AbstractBaseUser):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    # required mandatory to define
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=True)
    is_active        = models.BooleanField(default=True)
    is_superuser        = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name','phone_number']

    objects = MyAccountManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None): # if user is admin then he has all perm
        return self.is_admin or self.is_superuser

    def has_module_perms(self, add_label): 
        return True
    
# User Profile Model
class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE,related_name="profile")
    address = models.TextField(blank=True, max_length=100,null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    city = models.CharField(blank=True, max_length=100,null=True)
    pincode = models.CharField(blank=True,max_length=30,null=True)
    state = models.CharField(blank=True, max_length=20,null=True)
    country = models.CharField(blank=True, max_length=50)
    mobile = models.CharField(max_length=15,blank=True,null=True)

    def __str__(self):
        return self.user.username
    
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    
# step - 1 - Delete ALL APPS migrations file & existing db, after creating custom authentication
# step - 2 - run python manage.py runserver to generate blank db
# step - 3 - python manage.py make migrations
# step - 4 - python manage.py migrate