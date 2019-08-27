import sqlite3
import urllib.request
import urllib.parse
import re
from sqlite3 import Error
from .models import Project
import pages.constants as constants

def sql_query(form_data):
	data_qs = Project.project_db.all()
	temp1 = int(form_data['structure_type'])
	temp2 = int(form_data['building_material'])
	temp3 = int(form_data['service'])
	temp4 = int(form_data['construction_operation'])
	if temp1 != 0:
		data_qs = data_qs.filter(structure_type = temp1)
	if temp2 != 0:
		data_qs = data_qs.filter(building_material = temp2)
	if temp3 != 0:
		data_qs = data_qs.filter(service = temp3)
	if temp4 != 0:
		data_qs = data_qs.filter(construction_operation = temp4)
	return data_qs

def search(form):
	form_data = {
	'start_date': form.cleaned_data['start_date'],
	'end_date': form.cleaned_data['end_date'],
	'structure_type': form.cleaned_data['structure_type'],
	'building_material': form.cleaned_data['building_material'],
	'service': form.cleaned_data['service'],
	'construction_operation': form.cleaned_data['construction_operation'],
	'project_manager': form.cleaned_data['project_manager']
	}
	data_qs = sql_query(form_data)
	return data_qs