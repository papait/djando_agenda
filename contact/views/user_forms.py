from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from contact.forms import ContactForm, RegisterForm
from django.contrib import messages ,auth
from django.contrib.auth.forms import AuthenticationForm

def register(request: HttpRequest):
    
    form = RegisterForm()

    

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Usuário Registrado')
            return redirect('contact:index')

    return render(
        request,
        'contact/register.html',
        {
            'form' : form
        }
    )

def login_view(request : HttpRequest):

    form = AuthenticationForm(request=request)

    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request,user)
            messages.success(request,'Login com Sucesso')
            return redirect('contact:index')
        else:
            messages.error(request,'Login Invalido')
    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )

def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')