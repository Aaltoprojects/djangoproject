from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django_tables2 import RequestConfig
from .models import Project
from .tables import SearchResultTable
import urllib.request
import urllib.parse
import re
import pages.forms as forms
import pages.scripts.project_search as project_search
import pages.scripts.entries_to_database as entry_adder

def home(request):
	result = []
	if request.method == 'GET':
		form = forms.SearchProjectForm()
	elif request.method == 'POST':
		form = forms.SearchProjectForm(request.POST)
		if form.is_valid():
			result = project_search.search(form)
			result = SearchResultTable(result)
			RequestConfig(request).configure(result)
	return render(request, 'home.html', {'form':form, 'result':result})

def post_success(request):
	return render(request, 'snippets/success.html')

def edit_entry(request, project_id):
	current_project = Project.project_db.all().filter(id = project_id)[0]
	return render(request, 'edit_entry.html', {'row_data': current_project})

def add_entries_to_db(request):
    if request.method == 'GET':
        return render(request , 'add_entries_to_db.html', {'result': ""})
    elif request.method == 'POST':
        entry_adder.add_entries()
        return render(request , 'add_entries_to_db.html', {'result': "Done"})