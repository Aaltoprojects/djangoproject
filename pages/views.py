from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from .models import project
from pages.asiakastieto import haetiedot
from pages.search import search_database
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

def companysearch(request):

	if request.method == 'POST':

		form = forms.NameForm(request.POST)

		if form.is_valid():

			coname = form.cleaned_data['coname']
			coid = form.cleaned_data['coid']
			data = haetiedot(str(coname), str(coid))
			form = forms.NameForm()

			return render(request, 'graph.html', {'form':form, 'data':data})

	else:

		form = forms.NameForm()

	return render(request, 'searchcompany.html', {'form':form})


def search(request):

	if request.method == 'POST':

		form = forms.search_form(request.POST)
		if form.is_valid():
			search_emp = form.cleaned_data['search_field']
			
			if search_emp == "siivous":
				rows = search_database(7)
				return render(request, 'search.html', {'form':form, 'data':rows})
			elif search_emp == "tetsaus":
				rows = search_database(8)
				return render(request, 'search.html', {'form':form, 'data':rows})
			elif search_emp == "johtaminen":
				rows = search_database(9)
				return render(request, 'search.html', {'form':form, 'data':rows})

	else:
		form = forms.search_form()

	return render(request, 'search.html', {'form':form})


def create(request):

	if request.method == 'POST':

		emp = employees(
			name=request.POST['fname'],
			surname=request.POST['lname'],
			pnumber=request.POST['pnumber'],
			email=request.POST['email'],
			title=request.POST['title'],
			function=request.POST['function'],
			siivous=request.POST['siivous'],
			tetsaus=request.POST['tetsaus'],
			johtaminen=request.POST['johtaminen'],)
		emp.save()
		print('Creation successful')

		return render(request, 'created.html', {})

	else:

		return render(request, 'create.html', {})

def create_project(request):

	if request.method == 'GET':

		form = forms.Create_project()

		return render(request, 'add_project.html', {'form': form, 'data': []})

	elif request.method == 'POST':

		form = forms.Create_project(request.POST)

		if form.is_valid():

			instance = project(
				project_name = request.POST['project_name'],
				destination = request.POST['destination_name'],
				start_date = request.POST['start_date'],
				end_date = request.POST['end_date'],
				destination_type = request.POST['destination_type'],
				building_material = request.POST['building_material'],
				service = request.POST['service'],
				#HUOMAA KIRJOITUSVIRHE::::::::
				contruction_operation = request.POST['construction_operation'],
				specific_project_type = request.POST['specific_project_type'],
				project_description = request.POST['project_description'],
				documentation_path = request.POST['documentation_path'],
				project_manager = request.POST['project_manager']
				)
			instance.save()
			form = forms.Create_project()
			data = [instance.project_name,
					instance.destination,
					instance.start_date,
					instance.end_date,
					instance.destination_type,
					instance.building_material,
					instance.service,
					instance.contruction_operation,
					instance.specific_project_type,
					instance.project_description,
					instance.documentation_path,
					instance.project_manager]
		return render(request, 'add_project.html', {'form': form, 'data': data})