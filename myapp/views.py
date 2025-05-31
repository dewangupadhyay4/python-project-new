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
    error = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('task_list')
        else:
            error = "Invalid credentials"
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def task_list(request):
    tasks=Task.objects.filter(user=request.user)
    return render(request, 'task_list.html',{'tasks':tasks})

@login_required
def task_create(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.user=request.user
            task.save()
            return redirect('task_list')
    else:
        form=TaskForm()
    return render(request, 'task_form.html',{'form':form, 'title': 'cerate task'})

@login_required
def task_edit(request, pk):
    task=Task.objects.get(pk=pk,user=request.user)
    if request.method=='POST':
        form=TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form=TaskForm()
    return render(request,"task_form.html",{'form':form, 'title': 'Edit Task'})

@login_required
def task_delete(request,pk):
    task=Task.objects.get(pk=pk,user=request.user)
    if request.method=='POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html',{'task':task})
