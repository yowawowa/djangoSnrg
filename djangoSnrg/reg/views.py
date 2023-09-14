from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful')
            return redirect('Login')
        else:
            messages.error(request, 'Registration error')
    else:
        form = UserCreationForm()
    return render(request, 'reg/register.html', {'form': form})