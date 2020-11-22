from .models import Image,Profile,Comments
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


# Create your views here.
@login_required(login_url='/')
def main(request):
    user = request.user
    profile = Profile.get_profile()
    images = Image.images_get_all()
    comments = Comments.comments_get_all()
    return render(request, 'index.html', {'images':images,"profile":profile,"user":user,"comments":comments})

@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user
    profile = Profile.get_profile()
    image = Image.images_get_all()
    comments = Comment.comments_get_all()
    return render(request,'profile/profile.html',{"title":title,"comments":comments,"profile":profile,"image":image,"user":user})
                                                  
                                                  
                                                  
                                                  