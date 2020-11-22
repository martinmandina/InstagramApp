from .models import Image,Profile,Comments
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import UpdateProfileForm


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
    return render(request,'profile/profile.html',{"comments":comments,"profile":profile,"image":image,"user":user})

 @login_required(login_url='/accounts/login/')
def edit(request):
    title = 'Insta-Gram'
    current_user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            update = form.save(commit=False)
            update.user = current_user
            update.save()
            return redirect('profile')
    else:
        form = EditProfileForm()
    return render(request,'profile/update.html',{"form":form}) 
                                                
                                                  
                                                  
                                                  