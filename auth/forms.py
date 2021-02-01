from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class SignUpForm(UserCreationForm):
    email=forms.EmailField()
    firstname=forms.CharField()
    lastname=forms.CharField()
    class Meta:
        model=User
        fields=('username','password1','password2','email','firstname','lastname')
