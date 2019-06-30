from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from .forms import NameForm, create_employee_form, search_form
from .models import osaamisalue, projektit
from pages.asiakastieto import haetiedot
from pages.search import search_database
import urllib.request
import urllib.parse
import re

def home(request):

	return render(request, 'home.html', {})

def companysearch(request):

	if request.method == 'POST':

		form = NameForm(request.POST)

		if form.is_valid():

			coname = form.cleaned_data['coname']
			coid = form.cleaned_data['coid']
			data = haetiedot(str(coname), str(coid))
			form = NameForm()

			return render(request, 'graph.html', {'form':form, 'data':data})

	else:

		form = NameForm()

	return render(request, 'searchcompany.html', {'form':form})


def search(request):

	if request.method == 'POST':

		form = search_form(request.POST)
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
		form = search_form()

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

