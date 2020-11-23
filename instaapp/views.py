from .models import Image,Profile,Comments
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import UpdateProfileForm,UploadForm,NewCommentForm,InstaAppLetterForm
from .email import send_welcome_email


# Create your views here.
@login_required(login_url='/accounts/login/')
def main(request):
    present_user = request.user
    profile = Profile.get_profile()
    images = Image.images_get_all()
    comments = Comments.comments_get_all()
    form = 
    return render(request, 'index.html', {'images':images,"profile":profile,"present_user":present_user,"comments":comments})

@login_required(login_url='/accounts/login/')
def profile(request):
    present_user = request.user
    profile = Profile.get_profile()
    image = Image.images_get_all()
    comments = Comments.comments_get_all()
    return render(request,'profile/profile.html',{"comments":comments,"profile":profile,"image":image,"user":present_user})

@login_required(login_url='/accounts/login/')
def edit(request):
    present_user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            update = form.save(commit=False)
            update.user = present_user
            update.save()
            return redirect('profile')
    else:
        form = UpdateProfileForm()
    return render(request,'profile/update.html',{"form":form}) 
                                                
@login_required(login_url="/accounts/login/")
def results_search(request):
    present_user = request.user
    profile = Profile.get_profile()
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_name = Profile.search_profile(search_term)
        message = search_term

        return render(request,'search.html',{"profiles":profile,"user":present__user,"message":message,"username":searched_name})
                                                                  
    else:
        message = "Cant locate User"
        return render(request,'search.html',{"message":message})

@login_required(login_url="/accounts/login/")
def upload(request):
    present_user = request.user
    profiles = Profile.get_profile()
    for profile in profiles:
        if profile.user.id == present_user.id:
            if request.method == 'POST':
                form = UploadForm(request.POST,request.FILES)
                if form.is_valid():
                    upload = form.save(commit=False)
                    upload.user = present_user
                    upload.profile = profile
                    upload.save()
                    return redirect('home')
            else:
                form = UploadForm()
            return render(request,'fresh.html',{"user":present_user, "form":form})

@login_required(login_url='/accounts/login/')
def add_comment(request,pk):
    image = get_object_or_404(Image,pk=pk)
    present_user = request.user
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.user = present_user
            comment.save()
            return redirect('home')
    else:
        form = NewCommentForm()
    return render(request, 'comments.html', {"user":present_user,"comment_form":form})

@login_required(login_url="/accounts/login/")
def my_profile(request,pk):
    present_user = request.user
    images = Image.get_images()
    profile = Profile.get_profile()
    comments = Comments.get_comment()
    user = get_object_or_404(User, pk=pk)
    return render(request,'profile/myprofile.html',{"user":current_user,"images":images, "user":user,"comments":comments, "profile":profile})
                                               
                                              
                                               
                                              
                                            

                                                    
                                                  
                                          
                                                  
                                                  