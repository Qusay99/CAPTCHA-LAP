import django
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.http import request, HttpResponseRedirect
from django.views.generic.list import ListView
from django.shortcuts import redirect, render
from .forms import NewUserForm
from django.shortcuts import render 
from django.contrib.auth import authenticate, login as auth_login, logout

# Create your views here.
def main(request):
    return render(request, 'CAPTCHA_test/main.html')

def home(request):
    return render(request, 'CAPTCHA_test/.html')

def logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('blog-home')

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("main-site")

    form = AuthenticationForm()
    return render(request=request, template_name='CAPTCHA_test/login.html', context={"form":form})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect ("main/")
    form = NewUserForm
    return render(request=request, template_name='CAPTCHA_test/register.html', context={"form":form})
