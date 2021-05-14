from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required(login_url='/')
def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/')
def main(request):
    return render(request,"main.html")


def index(request):
    return render(request,"index.html")

@csrf_protect
def submit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')       
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/main')
        else:
            messages.error(request, 'Usuário ou senha inválida!')
    return redirect('/')
    