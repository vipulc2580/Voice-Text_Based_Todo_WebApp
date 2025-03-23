from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    # return HttpResponse('<h1>This is home Page</h1>')
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password=(form.cleaned_data['password1'])
            user.save()
            return redirect('login')
    else:
        form=UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})


def login_user(request):
    form=LoginForm(request.POST or None)
    
    if request.method=='POST' and form.is_valid():
        email=form.cleaned_data.get("email")
        password=form.cleaned_data.get("password")
        try:
            user = User.objects.get(email=email)  
            user = authenticate(request, username=user.username, password=password) 
        except User.DoesNotExist:
            user=None
        
        if user:
            login(request,user)
            # return HttpResponse("<h1>You've been logged In</h1>")
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid email or password,Please try again")

    return render(request,'registration/login.html',{'form':form})

@login_required
def logout_user(request):
    logout(request)
    return redirect('home')


@login_required
def todo_app(request):
    return render(request,'todo_app.html')