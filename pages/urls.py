from django.urls import path
from django.conf.urls import url
from . import views
import re

urlpatterns = [
	path('', views.home, name = 'home'),
	path('luo', views.create_project, name = 'add_project'),
	path('lisaamonta', views.add_entries_to_db, name = 'add_entries'),
	url(r'^edit/(?P<project_id>\w+)', views.edit_entry, name='edit_entry'),
]