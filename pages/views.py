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

def create_project(request):
	data = []
	if request.method == 'GET':
		form = forms.CreateProject()
		return render(request, 'add_project.html', {'form': form, 'data': data})
	elif request.method == 'POST':
		form = forms.CreateProject(request.POST)
		if form.is_valid():
			instance = Project(
			project_name = form.cleaned_data['project_name'],
			destination_name = form.cleaned_data['destination_name'],
			start_date = form.cleaned_data['start_date'],
			end_date = form.cleaned_data['end_date'],
			structure_type = form.cleaned_data['structure_type'],
			building_material = form.cleaned_data['building_material'],
			service = form.cleaned_data['service'],
			construction_operation = form.cleaned_data['construction_operation'],
			specific_project_type = form.cleaned_data['specific_project_type'],
			project_description = form.cleaned_data['project_description'],
			documentation_path = form.cleaned_data['documentation_path'],
			project_manager = form.cleaned_data['project_manager']
			)
			instance.save()
			form = forms.CreateProject()
			data = [instance.id,
					instance.project_name,
					instance.destination_name,
					instance.start_date,
					instance.end_date,
					instance.structure_type,
					instance.building_material,
					instance.service,
					instance.construction_operation,
					instance.specific_project_type,
					instance.project_description,
					instance.documentation_path,
					instance.project_manager]
		return render(request, 'add_project_preview.html', {'data': data})

def add_entries_to_db(request):
    if request.method == 'GET':
        return render(request , 'add_entries_to_db.html', {'result': ""})
    elif request.method == 'POST':
        entry_adder.add_entries()
        return render(request , 'add_entries_to_db.html', {'result': "Done"})