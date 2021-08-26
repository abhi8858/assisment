from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .form import LoginForm,SignUpForm

# Create your views here.

def home(request):
    return render(request,'core/home.html')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                messages.success(request,f'Hi {uname} you are successfully logged in !!')
                return redirect('home')
        else:
            form=LoginForm()
        context={
            'form':form,
            'login_active':'active',
            'login_disabled':'disabled'
            }
        return render(request,'core/login.html',context)
    else:
        return redirect('home')

def user_logout(request):
	logout(request)
	messages.warning(request,'You are successfully logged out !!')
	return redirect('home')

def user_signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Signed up successfully !!')
            user=form.save()
            login(request,user)
            return redirect('home')
    else:
        form=SignUpForm()
    context={
        'form':form,
        'signup_active':'active',
        'signup_disabled':'disabled'
    }
    return render(request,'core/signup.html',context)