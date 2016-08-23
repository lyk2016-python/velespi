from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout
)

from profiles.forms import RegistrationForm, LoginForm


def register(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.info(
                request,
                'Kayıt başarılı. Şimdi login olabilirsiniz.'
            )

            return redirect('login')

    return render(request, 'register.html', {
        'form': form,
    })


def login(request):
    if request.user.is_authenticated:
        return redirect('/')  # profil sayfasına yönlendirilecek

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            auth_login(request, form.user)
            messages.info(
                request,
                'Giriş yaptınız.'
            )

        return redirect('/')

    return render(request, 'login.html', {
        'form': form
    })


def logout(request):
    auth_logout(request)
    return redirect('/')
