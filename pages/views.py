from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from .models import Project
import urllib.request
import urllib.parse
import re
import pages.forms as forms
import pages.project_search as searcher

def home(request):
	result = ""
	if request.method == 'POST':
		form = forms.SearchProjectForm(request.POST)
		if form.is_valid():
			result = searcher.project_search(form)
	elif request.method == 'GET':
		form = forms.SearchProjectForm()
	
	return render(request, 'home.html', {'form':form, 'result':result})

def create_project(request):
	if request.method == 'GET':
		form = forms.CreateProject()
		return render(request, 'add_project.html', {'form': form, 'data': []})
	elif request.method == 'POST':
		form = forms.CreateProject(request.POST)

		if form.is_valid():
			instance = Project(
				project_name = request.POST['project_name'],
				destination_name = request.POST['destination_name'],

				start_date = request.POST['start_date_year'] 
				+ '-' + request.POST['start_date_month'].zfill(2) 
				+ '-' + request.POST['start_date_day'].zfill(2),

				end_date = request.POST['end_date_year']
				+ '-' + request.POST['end_date_month'].zfill(2)
				+ '-' + request.POST['end_date_day'].zfill(2),

				structure_type = request.POST['structure_type'],
				building_material = request.POST['building_material'],
				service = request.POST['service'],
				construction_operation = request.POST['construction_operation'],
				specific_project_type = request.POST['specific_project_type'],
				project_description = request.POST['project_description'],
				documentation_path = request.POST['documentation_path'],
				project_manager = request.POST['project_manager']
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