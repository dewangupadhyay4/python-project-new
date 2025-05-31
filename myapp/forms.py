from  django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import forms

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']