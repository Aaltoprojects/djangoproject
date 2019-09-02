from django.urls import path
from django.conf.urls import url
from . import views
import re
from pages.formpreview import CreateProjectPreview
from pages.forms import CreateProjectForm
from django import forms

urlpatterns = [
	path('lisaamonta', views.add_entries_to_db, name = 'add_entries'),
	path('', views.home, name = 'home'),
	url(r'^view/(?P<project_id>\w+)', views.view_entry, name='view_entry'),
	url(r'^post/$', CreateProjectPreview(CreateProjectForm), name = 'add_project'),
	path('success', views.post_success),
]