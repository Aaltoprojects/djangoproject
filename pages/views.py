from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.core import mail

import datetime as dt
import pages.models as models
import urllib.request
import urllib.parse
import re
from pages.constants import DATE_FORMAT
from pages.forms import CreateProjectForm, SearchProjectForm, AddFilterForm
from django import forms
import pages.scripts.sql_util as sql_util
import pages.scripts.parse_util as parse_util


@login_required(login_url='/login/')
def home(request):
    form = SearchProjectForm(request.GET)
    f1, f2, f3, f4, f5 = sql_util.get_filters()
    result = []
    context = {'form': form,
               'f1': f1,
               'f2': f2,
               'f3': f3,
               'f4': f4,
               'f5': f5,
               'result': result,
               }
    return render(request, 'home.html', context)


@login_required(login_url='/login/')
def search_project(request):
  if request.method == 'GET':
    f1, f2, f3, f4, f5 = sql_util.get_filters()
    input_data = request.GET.copy()
    result = sql_util.search(input_data)
    context = {'f1': f1,
               'f2': f2,
               'f3': f3,
               'f4': f4,
               'f5': f5,
               'result': result,
    }
  return render(request, 'snippets/ajax_result_table.html', context)


@login_required(login_url='/login/')
def add_project(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            input_data = request.POST.copy()
            sql_util.save_entry_to_db(form, input_data)
            return render(request, 'snippets/success.html')
    f1, f2, f3, f4, f5 = sql_util.get_filters()
    form = CreateProjectForm()
    context = {'form': form,
               'f1': f1,
               'f2': f2,
               'f3': f3,
               'f4': f4,
               'f5': f5,
               }
    return render(request, 'add_project.html', context)


@login_required(login_url='/login/')
def edit_project(request, id):
    project = models.Project.project_db.get(id=id)
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            input_data = request.POST.copy()
            sql_util.edit_entry_in_db(project, form, input_data)
            return render(request, 'snippets/success.html')
    f1, f2, f3, f4, f5 = sql_util.get_filters()
    filters_qset = project.filters.all()
    filters_dict = parse_util.filters_qs_to_dict(filters_qset)
    form = CreateProjectForm(initial={'project_name': project.project_name,
                                      'destination_name': project.destination_name,
                                      'start_date': dt.datetime.strptime(str(project.start_date),
                                                                         '%Y-%m-%d').strftime(DATE_FORMAT),
                                      'end_date': dt.datetime.strptime(str(project.end_date),
                                                                       '%Y-%m-%d').strftime(DATE_FORMAT),
                                      'keywords': project.keywords,
                                      'project_description': project.project_description,
                                      'documentation_path': project.documentation_path,
                                      'project_manager': project.project_manager,
                                      })
    context = {'form': form,
               'f1': f1,
               'f2': f2,
               'f3': f3,
               'f4': f4,
               'f5': f5,
               'sf1': filters_dict['Rakennustyyppi'],
               'sf2': filters_dict['Rakennusmateriaali'],
               'sf3': filters_dict['Palvelu'],
               'sf4': filters_dict['Rakennustyyppi'],
               'sf5': filters_dict['Rakenneosa'],
               }
    return render(request, 'edit_project.html', context)


@login_required(login_url='/login/')
def post_success(request):
    return render(request, 'snippets/success.html')


@user_passes_test(lambda u: u.is_superuser,login_url='/admin/login/')
def add_filter(request):
    indicator = 'NOT EXISTS'
    if request.method == 'POST':
        add_filter_form = AddFilterForm(request.POST)
        if add_filter_form.is_valid():
            matching_qs = sql_util.check_if_exists_in_db(add_filter_form)
            if not matching_qs:
                new_filter = add_filter_form.save()
            else:
                indicator = 'EXISTS'
    add_filter_form = AddFilterForm()
    context = {'form': add_filter_form,'indicator': indicator,}
    return render(request, 'add_filter.html', context)

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
        request.META["HTTP_HOST"] + "/confirm?token=" + user.username
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
