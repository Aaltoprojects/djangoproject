import sqlite3
import urllib.request
import urllib.parse
import re
from sqlite3 import Error

def project_search(form):
	form_data = {
	'start_date': form.cleaned_data['start_date'],
	'end_date': form.cleaned_data['end_date'],
	'destination_type': form.cleaned_data['destination_type'],
	'building_material': form.cleaned_data['building_material'],
	'service': form.cleaned_data['service'],
	'construction_operation': form.cleaned_data['construction_operation'],
	'free_description': form.cleaned_data['free_description'],
	'project_manager': form.cleaned_data['project_manager'],
	}

	#if this value is 0, no filters have been applied
	sum_values = int(form_data['destination_type'])+int(form_data['building_material'])+int(form_data['service'])+int(form_data['construction_operation'])
	first = True
	cond_str = ""
	if sum_values != 0:
		cond_str = " WHERE"
		if int(form_data['destination_type']) != 0:
			if first:
				first = False
				cond_str += " destination_type = :value1"
			else:
				cond_str += " AND destination_type = :value1"
		if int(form_data['building_material']) != 0:
			if first:
				first = False
				cond_str += " building_material = :value2"
			else:
				cond_str += " AND building_material = :value2"
		if int(form_data['service']) != 0:
			if first:
				first = False
				cond_str += " service = :value3"
			else:
				cond_str += " AND service = :value3"
		if int(form_data['construction_operation']) != 0:
			if first:
				first = False
				cond_str += " contruction_operation = :value4"
			else:
				cond_str += " AND contruction_operation = :value4"

	database = "db.sqlite3"
	connection = create_connection(database)
	cursor = connection.cursor()
	current = cursor.execute("SELECT project_name, specific_project_type FROM pages_project" + cond_str,
	{
	'value1':form_data['destination_type'],
	'value2':form_data['building_material'],
	'value3':form_data['service'],
	'value4':form_data['construction_operation']
	})

	return current.fetchall()

def create_connection(db_file):
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as err:
		print(err)
	return None