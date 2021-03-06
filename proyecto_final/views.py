from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from proyecto_final.forms import User_registration_form

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                context = {'message':f'Usted se ha logueado bajo el nombre de {username}!!'}
                return render(request, 'index.html', context = context)
            else:
                context = {'errors':'No hay ningun usuario con esas credenciales!!!'}
                form = AuthenticationForm()
                return render(request, 'auth/login.html', context = context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors':errors, 'form':form} 
            return render(request, 'auth/login.html', context = context)

    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'auth/login.html', context = context)


def register_view(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            context = {'message':f'Usuario creado correctamente, bienvenido {username}'}
            return render(request, 'index.html', context = context)
        else:
            errors = form.errors
            form = User_registration_form()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth/register.html', context = context)
    else:
        form = User_registration_form()
        context = {'form':form}
        return render(request, 'auth/register.html', context =context)



def logout_view(request):
    logout(request)
    return redirect('index')

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.user.is_authenticated:
        print(request.user.username)
        return render(request, 'contact.html')
    else:
        return redirect('login')
    
def leandro(request):
    if request.user.is_authenticated:
        print(request.user.username)
        return render(request,'leandro.html')
    else:
        return redirect('login')

def luciano(request):
    if request.user.is_authenticated:
        print(request.user.username)
        return render(request,'luciano.html')
    else:
        return redirect('login')  
    
def lautaro(request):
    if request.user.is_authenticated:
        print(request.user.username)
        return render(request,'lautaro.html')
    else:
        return redirect('login')       
    
def about(request):
    if request.user.is_authenticated:
        print(request.user.username)
        return render(request,'about.html')
    else:
        return redirect('login')   