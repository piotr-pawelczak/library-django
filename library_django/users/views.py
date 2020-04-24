from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response, 'User successfully registered')
            return redirect('../login/')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(response, 'users/register.html', context)

