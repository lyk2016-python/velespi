from django.shortcuts import render, redirect
from django.contrib import messages
from profiles.forms import RegistrationFrom, LoginForm
from django.contrib.auth import (login as auth_login,
                                 logout as auth_logout)


def register(request):
    form = RegistrationFrom()

    if request.method == 'POST':
        form = RegistrationFrom(request.POST)

        if form.is_valid():
            form.save()

            messages.info(request,
                          'Registration successful! You can now login.')

            return redirect('login')

    return render(request, 'register.html', {
        'form': form,
    })


def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            auth_login(request, form.user)
            messages.info(request,
                          'Welcome')

    return render(request, 'login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('/')