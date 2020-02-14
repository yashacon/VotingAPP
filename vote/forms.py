from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Userprofile

class ExtendedUserCreationForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']

    

class UserprofileForm(forms.ModelForm):
    class Meta:
        model=Userprofile
        fields=['display_picture']
