from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from .forms import NameForm, create_employee_form
from .models import employees
from pages.asiakastieto import haetiedot
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

		if form.is_valid():

			return render(request, search.html, {'form':form})

	return render(request, 'search.html', {})


def create(request):

	if request.method == 'POST':

		return render(request, 'created.html', {})

	return render(request, 'create.html', {})

