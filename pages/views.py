from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import NameForm, create_employee_form, search_employee_form
from .models import employee
from pages.asiakastieto import haetiedot
import urllib.request
import urllib.parse
import re

def home(request):
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
	return render(request, 'home.html', {'form':form})


def about(request):
	if request.method == 'POST':
		form = create_employee_form(request.POST)
		if form.is_valid():
			fname = form.cleaned_data['fname']
			sname = form.cleaned_data['surname']
			tit = form.cleaned_data['title']
			func = form.cleaned_data['function']
			emp = employee(name = fname, surname = sname, title = tit, function = func)
			emp.save()
			form = NameForm()
			return render(request, 'home.html', {'form':form})
	else:
		form = create_employee_form()
	return render(request, 'about.html', {'form':form})

def search(request):
	if request.method == 'POST':
		form = search_employee_form(request.POST)
		if form.is_valid():
			func = form.cleaned_data['function']
			obj = employee.objects.all()
			data = {}
			form = search_employee_form()
			return render(request, 'searchres.html', {'data':obj})
	else:
		form = search_employee_form()
	return render(request, 'search.html', {'form':form})