from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.core import mail
from django.core.exceptions import ObjectDoesNotExist
from django.apps import apps
import pages.models as models
import urllib.request
import urllib.parse
import re
from pages.constants import DATE_FORMAT
from pages.forms import CreateProjectForm, SearchProjectForm, AddFilterForm, CreateReferenceProjectForm
from django import forms
import pages.scripts.sql_util as sql_util
import pages.scripts.parse_util as parse_util
from django.urls import reverse
from attachments.models import Attachment, Image
from attachments.forms import AttachmentForm, ImageForm
import attachments.views
from django.utils.datastructures import MultiValueDict
from attachments.views import delete_image
from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@login_required(login_url='/login/')
def home(request):
    form1 = SearchProjectForm()
    context = {'form1': form1,
               'filters':sql_util.get_filters(),
               }
    return render(request, 'home.html', context)


@login_required(login_url='/login/')
def success(request):
    return render(request, 'snippets/success.html')


@login_required(login_url='/login/')
def search_project(request):
    f1, f2, f3, f4, f5 = sql_util.get_filters()
    input_data = request.GET.copy()
    result = sql_util.search(input_data)
    context = {
               'filters':sql_util.get_filters(),
               'result': result,
               }
    return render(request, 'snippets/ajax_result_table.html', context)


@login_required(login_url='/login/')
def add_project(request):
    if request.method == 'POST':
        form1 = CreateProjectForm(request.POST)
        input_data = request.POST.copy()
        if form1.is_valid():
            obj1 = sql_util.save_entry_to_db(form1, input_data)
            pk = obj1.id
            app_label = 'pages'
            model_name = 'Project'
            if request.user.has_perm("attachments.add_attachment"):
              model = apps.get_model(app_label, model_name)
              obj = get_object_or_404(model, pk=pk)
              files = request.FILES.getlist('attachment_file')
              images = request.FILES.getlist('attachment_image')
              if len(files) > 0:
                for f in files:
                    test = MultiValueDict({'attachment_file': [f]})
                    form = AttachmentForm(request.POST, test)
                    if form.is_valid():
                        form.save(request, obj)
              if len(images) > 0:
                for i in images:
                    test = MultiValueDict({'attachment_image': [i]})
                    form = ImageForm(request.POST, test)
                    if form.is_valid():
                        form.save(request, obj)
            if 'undertaking' in input_data:
                form2 = CreateReferenceProjectForm(request.POST)
                if form2.is_valid():
                    obj2 = sql_util.save_ref_to_db(form2, obj1)
            return HttpResponseRedirect(reverse('success'))
        else: 
            f1, f2, f3, f4, f5 = sql_util.get_filters()
            input_data = request.POST.copy()
            filters_qset = parse_util.parse_input_filters(input_data)
            filters_dict = parse_util.filters_qs_to_dict(filters_qset)
            attachment_model = Attachment(pk=1) # tää on viel kyssäri
            image_model = Image(pk=1)
            context = {'form': form,
                       'attachment': attachment_model,
                       'image': image_model,
                       'filters':sql_util.get_filters(),
                       'selected_filters': parse_util.filters_qs_to_dict(project.filters.all())
                       }
            return render(request, 'add_project.html', context)
    elif request.method == 'GET':
        f1, f2, f3, f4, f5 = sql_util.get_filters()
        form1 = CreateProjectForm()
        form2 = CreateReferenceProjectForm()
        attachment_model = Attachment(pk=1) # tää on viel kyssäri
        image_model = Image(pk=1)
        context = {'form1': form1,
                   'form2': form2,
                   'attachment': attachment_model,
                   'image': image_model,
                   'filters':sql_util.get_filters(),
                   }
        return render(request, 'add_project.html', context)

@login_required(login_url='/login/')
def edit_project(request, id):
    project = models.Project.project_db.get(id=id)
    if request.method == 'POST':
        form1 = CreateProjectForm(request.POST)
        if form1.is_valid():
            input_data = request.POST.copy()
            sql_util.edit_entry_in_db(project, form1, input_data)
            app_label = 'pages'
            model_name = 'Project'
            if request.user.has_perm("attachments.add_attachment"):
                model = apps.get_model(app_label, model_name)
                obj = get_object_or_404(model, pk=id)
                files = request.FILES.getlist('attachment_file')
                images = request.FILES.getlist('attachment_image')
                if len(files) > 0:
                    for f in files:
                        test = MultiValueDict({'attachment_file': [f]})
                        form = AttachmentForm(request.POST, test)
                        if form.is_valid():
                          form.save(request, obj)
                if len(images) > 0:
                    existing_images = Image.objects.attachments_for_object(id)
                    for image in existing_images:
                      delete_image(request, image.pk)
                    for i in images:
                      test = MultiValueDict({'attachment_image': [i]})
                      form = ImageForm(request.POST, test)
                      if form.is_valid():
                        form.save(request, obj)
            if 'undertaking' in input_data:
                form2 = CreateReferenceProjectForm(request.POST)
                if form2.is_valid():
                    sql_util.edit_ref_in_db(project.referenceproject, form2)
            return HttpResponseRedirect(reverse(success))
    elif request.method == 'GET':
      f1, f2, f3, f4, f5 = sql_util.get_filters()
      filters_qset = project.filters.all()
      filters_dict = parse_util.filters_qs_to_dict(filters_qset)
      form1 = CreateProjectForm(
          initial={
              'project_name': project.project_name,
              'destination_name': '' if project.destination_name == '—' else project.destination_name,
              'start_date': parse_util.format_time(project.start_date),
              'end_date': parse_util.format_time(project.end_date),
              'keywords': ''  if project.keywords == '—' else project.keywords,
              'project_description': project.project_description,
              'documentation_path': ''  if project.documentation_path == '—' else project.documentation_path,
              'project_manager': ''  if project.project_manager == '—' else project.project_manager,
          })
      try:
          form2 = CreateReferenceProjectForm(
              initial={
                  'undertaking': project.referenceproject.undertaking,
                  'client': project.referenceproject.client,
                  'area': project.referenceproject.area,
                  'construction_cost': project.referenceproject.construction_cost,
                  'project_accepted': parse_util.format_time(project.referenceproject.project_accepted),
                  'construction_permit_granted': parse_util.format_time(project.referenceproject.construction_permit_granted),
              })
      except ObjectDoesNotExist:
          form2 = False
      attachment_model = Attachment(pk=1)
      image_model = Image(pk=1)
      context = {'form1': form1,
                 'form2': form2,
                 'attachment': attachment_model,
                 'image': image_model,
                 'id': id,
                 'filters': sql_util.get_filters(),
                 'selected_filters': parse_util.filters_qs_to_dict(project.filters.all())
                 }
      return render(request, 'edit_project.html', context)


@user_passes_test(lambda u: u.is_superuser, login_url='/admin/login/')
def add_filter(request):
    showMessage = True
    success = True
    if request.method == 'POST':
        add_filter_form = AddFilterForm(request.POST)
        if add_filter_form.is_valid():
            matching_qs = sql_util.check_if_exists_in_db(add_filter_form)
            if not matching_qs:
                new_filter = add_filter_form.save()
                add_filter_form = AddFilterForm()
                showMessage = True
                success = True
            else:
                success = False
                showMessage = True
    elif request.method == 'GET':
        add_filter_form = AddFilterForm()
        showMessage = False
        success = False
    context = {'form': add_filter_form, 'success':success, 'showMessage':showMessage}
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
