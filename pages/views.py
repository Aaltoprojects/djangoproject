from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import mail

import pages.models as models
import urllib.request
import urllib.parse
import re
from pages.forms import CreateProjectForm, SearchProjectForm, AddFilterForm
from django import forms
import pages.scripts.project_search as project_search
import pages.scripts.sql_util as sql_util
import pages.scripts.parse_util as parse_util

@login_required(login_url='/login/')
def home(request):
    form = SearchProjectForm(request.GET)
    f1,f2,f3,f4,f5 = sql_util.get_filters()
    result = []
    context = {'form': form,
                'f1': f1,
                'f2': f2,
                'f3': f3,
                'f4': f4,
                'f5': f5,
                'result': result,
                }
    if form.is_valid():
        result = []
        #context['result'] = project_search.search(form)
    return render(request, 'home.html', context)

@login_required(login_url='/login/')
def add_project(request):
    f1,f2,f3,f4,f5 = sql_util.get_filters()
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            input_filters = parse_util.parse_input_filters(data)
            obj = models.Project(
            project_name = form.cleaned_data['project_name'],
            destination_name = form.cleaned_data['destination_name'],
            start_date = form.cleaned_data['start_date'],
            end_date = form.cleaned_data['end_date'],
            keywords = form.cleaned_data['keywords'],
            project_description = form.cleaned_data['project_description'],
            documentation_path = form.cleaned_data['documentation_path'],
            project_manager = form.cleaned_data['project_manager'],
            )
            obj.save()
            for f in input_filters:
                obj.filters.add(f)
            return render(request, 'snippets/success.html')
    form = CreateProjectForm()
    context = {'form': form,
    'f1': f1,
    'f2': f2,
    'f3': f3,
    'f4': f4,
    'f5': f5,
    }
    return render(request, 'add_project.html', context)

def post_success(request):
	return render(request, 'snippets/success.html')

@login_required(login_url='/login/')
def add_filter(request):
    if request.method == 'POST':
        form = AddFilterForm(request.POST)
        if form.is_valid():
            new_filter = form.save()
    form = AddFilterForm()
    return render(request, 'add_filter.html', {'form': form})

# Signup and login functionalities:

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text='Syötä toimiva sähköpostiosoite.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

def confirmUser(request):
    username = request.GET.get("token")
    user = get_object_or_404(User, username=username)
    user.is_active = True
    user.save()
    return render(request, "registration/confirmed.html")

def logout(request):
    logout(request)
    return render(request, 'registration/signup.html')

def send_email(request, user):
    subject1 = "Osaamispankin sähköpostivahvistus"
    body1 = "Vahvista käyttäjä klikkaamalla linkkiä: http://" + \
        request.META["HTTP_HOST"]+"/confirm?token="+user.username
    from1 = "xX_m4s73rG4m3r_Xx@a.shop"
    to1 = user.email
    with mail.get_connection() as connection:
        mail.EmailMessage(
            subject1, body1, from1, [to1],
            connection=connection,
        ).send()

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)
            user.is_active = False
            user.save()
            # login(request, user)
            send_email(request, user)
            return render(request, 'registration/pleaseConfirm.html')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})