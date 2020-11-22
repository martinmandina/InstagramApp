from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    profilePhoto =  models.ImageField(upload_to='profile/',null=True,blank=True)
    bio = models.CharField(max_length=60,blank=True)

    
