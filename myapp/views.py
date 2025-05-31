from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

def signup_view(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form=SignupForm()
    return render(request,"signup.html",{'form':form})
