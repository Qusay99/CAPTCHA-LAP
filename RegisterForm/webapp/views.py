import django
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.http import request, HttpResponseRedirect
from django.views.generic.list import ListView
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Content, Document
from .forms import CommentForm, ContentForm, NewUserForm, DocumentForm
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from django.contrib.auth import authenticate, login as auth_login, logout

# Create your views here.


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect ("main/")
    form = NewUserForm
    return render(request=request, template_name='webapp/register.html', context={"form":form})


