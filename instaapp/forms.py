from django import forms
from django.contrib.auth.models import User
from .models import Image,Profile,Comments

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']