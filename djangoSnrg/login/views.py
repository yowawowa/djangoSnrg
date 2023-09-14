from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserLoginForm


# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, 'Login error')
    else:
        form = UserLoginForm(request.POST)
    return render(request, 'login/login.html', {'form': form})


# TODO username showing on navbar after logout
def user_logout(request):
    logout(request)
    return redirect('Login')
