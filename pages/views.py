from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from .models import Project
import urllib.request
import urllib.parse
import re
import pages.forms as forms
import pages.project_search

def home(request):
	result = []
	if request.method == 'GET':
		form = forms.SearchProjectForm()
	elif request.method == 'POST':
		form = forms.SearchProjectForm(request.POST)
		if form.is_valid():
			result = pages.project_search.search(form)
		form = forms.SearchProjectForm()
	
	return render(request, 'home.html', {'form':form, 'result':result})

def create_project(request):
	data = []
	if request.method == 'GET':
		form = forms.CreateProject()
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

			data = [instance.project_name,
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

	return render(request, 'add_project.html', {'form': form, 'data': data})