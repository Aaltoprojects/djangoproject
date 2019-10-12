from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django_tables2 import RequestConfig
import pages.models as models
from .tables import SearchResultTable
import urllib.request
import urllib.parse
import re
import pages.forms as forms
import pages.scripts.project_search as project_search

def home(request):
	form = forms.SearchProjectForm(request.GET)
	if form.is_valid():
		result = project_search.search(form)
	return render(request, 'home.html', {'form':form, 'result':result})

def post_success(request):
	return render(request, 'snippets/success.html')

def view_entry(request, project_id):
	current_project = models.Project.project_db.all().filter(id = project_id)[0]
	return render(request, 'view_entry.html', {'row_data': current_project})