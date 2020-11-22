from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    profilePhoto =  models.ImageField(upload_to='profile/',null=True,blank=True)
    bio = models.CharField(max_length=60,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


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

    def __str__(self):
        return self.image_name

    def image_save(self):
        self.save()

    def image_delete(self):
        self.delete()

    @classmethod
    def images_get_all(cls):
        image =  Image.objects.all()
        return image

    @classmethod
    def get_image_by_id(cls,id):
        image = Image.objects.filter(id=Image.id)
        return image

    @classmethod
    def caption_update(cls,id,image_caption):
        captionn = Image.objects.filter(id=id).update(image_caption = image_caption)
        return captionn

class Comments(models.Model):
    comments = models.CharField(max_length=60,blank=True,null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comments

    def comment_save(self):
        self.save()

    def comment_delete(self):
        self.delete

    @classmethod
    def comments_get_all(cls):
        comments = Comments.objects.all()
        return comments








