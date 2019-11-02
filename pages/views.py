from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
import pages.models as models
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
	return render(request, 'home.html', {'form':form})

def post_success(request):
	return render(request, 'snippets/success.html')