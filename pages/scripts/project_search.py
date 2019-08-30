import sqlite3
import urllib.request
import urllib.parse
import re
from sqlite3 import Error
from pages.models import Project
import pages.constants as constants
from django.db.models import Q

def sql_query(form_data):
	data_qs = Project.project_db.all()
	temp1 = int(form_data['structure_type'])
	temp2 = int(form_data['building_material'])
	temp3 = int(form_data['service'])
	temp4 = int(form_data['construction_operation'])
	temp5 = str(form_data['key_phrase_search'])
	print(temp5)
	if temp1 != 0:
		data_qs = data_qs.filter(structure_type = temp1)
	if temp2 != 0:
		data_qs = data_qs.filter(building_material = temp2)
	if temp3 != 0:
		data_qs = data_qs.filter(service = temp3)
	if temp4 != 0:
		data_qs = data_qs.filter(construction_operation = temp4)
	if temp5 != "":
		qset = Q()
		for term in temp5.split():
			tmp = Q()
			tmp |= Q(destination_name__contains=term)
			tmp |= Q(project_name__contains=term)
			tmp |= Q(specific_project_type__contains=term)
			tmp |= Q(project_description__contains=term)
			tmp |= Q(documentation_path__contains=term)
			tmp |= Q(project_manager__contains=term)
			qset &= tmp
		data_qs = data_qs.filter(qset)
	return data_qs

def search(form):
	form_data = {
	'start_date': form.cleaned_data['start_date'],
	'end_date': form.cleaned_data['end_date'],
	'structure_type': form.cleaned_data['structure_type'],
	'building_material': form.cleaned_data['building_material'],
	'service': form.cleaned_data['service'],
	'construction_operation': form.cleaned_data['construction_operation'],
	'project_manager': form.cleaned_data['project_manager'],
	'key_phrase_search': form.cleaned_data['key_phrase_search']
	}
	data_qs = sql_query(form_data)
	return data_qs