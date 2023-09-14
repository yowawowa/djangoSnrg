from django.contrib import messages
from django.contrib.auth import login
from reg.forms import UserRegisterForm
from django.shortcuts import render, redirect

# Create your views here.
from login.views import user_login


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful')
            user = form.save()
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, 'Registration error')
    else:
        form = UserRegisterForm()
    return render(request, 'reg/register.html', {'form': form})
