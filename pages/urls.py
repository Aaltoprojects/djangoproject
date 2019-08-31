from django.urls import path
from django.conf.urls import url
from . import views
import re
from pages.formpreview import SomeModelFormPreview
from pages.forms import CreateProject
from django import forms

urlpatterns = [
	path('lisaamonta', views.add_entries_to_db, name = 'add_entries'),
	#delete when project ready ^
	path('', views.home, name = 'home'),
	url(r'^edit/(?P<project_id>\w+)', views.edit_entry, name='edit_entry'),
	url(r'^post/$', SomeModelFormPreview(CreateProject), name = 'add_project'),
	path('success', views.post_success),
]