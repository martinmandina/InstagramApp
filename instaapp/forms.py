from django import forms
from django.contrib.auth.models import User
from .models import Image,Profile,Comments

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes','profile']

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user','image',]

class InstaAppLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
