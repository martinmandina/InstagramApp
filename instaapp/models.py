from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    profilePhoto =  models.ImageField(upload_to='profile/',null=True,blank=True)
    bio = models.CharField(max_length=60,blank=True)

    def __str__(self):
        return self.bio

    def profile_save(self):
        self.save()

    def profile_delete(self):
        self.delete()

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()
        return profile

    @classmethod
    def search_profile(cls,search_term):
        profile = cls.objects.filter(user__username__icontains=search_term)
        return profile

    @classmethod
    def update_profile(cls,id,bio):
        updated = Image.objects.filter(id=id).update(bio = bio)
        return updated

class Image(models.Model):
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    image_name = models.CharField(max_length = 50)
    image_caption =  models.CharField(max_length = 60)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.BooleanField(default=False)


