from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from app_login.models import Profile
from app_login.forms import ProfileForm,SignUpForm

from django.contrib import messages

def signup(request):
    form=SignUpForm()
    if request.method == 'POST':
        form=SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Account Created Successfully !!!')
            return HttpResponseRedirect(reverse('app_login:login'))
    return render(request,'app_login/signup.html',context={'form':form})

def login_user(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.cleaned_data.get('username')
            passw=form.cleaned_data.get('password')

            user=authenticate(username=user,password=passw)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('app_shop:home'))
    return render(request, 'app_login/login.html', context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('app_shop:home'))

@login_required
def profile(request):
    profile=Profile.objects.get(user=request.user)
    form=ProfileForm(instance=profile)

    if request.method == 'POST':
        form=ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Updated Successfully !!!')
            form=ProfileForm(instance=profile)
    return render(request,'app_login/profile_change.html',context={'form':form  })
