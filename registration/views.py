from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from blog.models import UserProfile

from .forms import *
from .decorators import *


@login_required(login_url='registration:login')
@redirect_unauthenticated_user_to_login
def homepage(request):
    return redirect('blog:home')

@unauthenticated_user
def user_signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()

            UserProfile.objects.create(user=user)

            user = form.cleaned_data.get('username')
            messages.success(request, 'An account was created for ' + user)

            return redirect('registration:login')

    context = {
        'form': form,
    }
    return render(request, 'registration/signup.html', context)

@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, password=password, username=username)

        if user is not None:
            login(request, user)
            return redirect('blog:home')
        else:
            messages.info(request, 'Username OR Password is incorrect!')

    context = {}
    return render(request, 'registration/login.html', context)

def logout_user(request):
    logout(request) 
    return redirect('registration:login')
