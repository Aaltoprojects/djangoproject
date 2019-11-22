from django.urls import path
from django.conf.urls import url, include
from . import views
import re
from pages.form_preview import CreateProjectPreview
from pages.forms import CreateProjectForm
from django import forms

urlpatterns = [
	path('', views.home, name = 'home'),
    path('', include('django.contrib.auth.urls')),
    url(r'^signup/$', views.signup, name='signup'),
    path('confirm', views.confirmUser, name='User confirmed'),
    path('logout/', views.logout, name='logout'),
	url(r'^post/$', CreateProjectPreview(CreateProjectForm), name = 'add_project'),
	path('success', views.post_success),
]