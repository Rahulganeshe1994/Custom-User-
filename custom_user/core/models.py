from django.db import models
from django.contrib.auth.models import AbstractUser

# Creating Custom User Model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to='user_profile',blank=True,null=True)
    address = models.CharField(max_length=50,blank=True,null=True)
    phone = models.CharField(max_length=11,blank=True,null=True)
    role = models.CharField(max_length=50,blank=True,null=True)
    bio = models.TextField(blank=True,null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    def __str__(self):
        return self.email
