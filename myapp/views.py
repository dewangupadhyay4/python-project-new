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

def login_view(request):
    if request.method=='POST':
        user=authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('task_list')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect("login")

def task_list(request):
    tasks=Task.objects.filter(user=request.user)
    return render(request, 'task_list.html',{'tasks':tasks})
