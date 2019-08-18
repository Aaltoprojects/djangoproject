import sqlite3
import urllib.request
import urllib.parse
import re
from sqlite3 import Error
import pages.constants as constants

def sum_filters(form_data):
	sum = 0
	for filter, _ in constants.ELEMS_DICT.items():
		sum += int(form_data[filter])
	return sum

def create_sql_query(form_data):
	sum_values = sum_filters(form_data)
	first = True
	cond_str = ''
	if sum_values != 0:
		cond_str = ' WHERE'
		for filter, value in constants.ELEMS_DICT.items():
			if int(form_data[filter]) != 0:
				if first:
					first = False
					cond_str += ' ' + filter +  ' = ' + value
				else:
					cond_str += ' AND ' + filter + ' = ' + value
	return 'SELECT * FROM pages_project' + cond_str

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

	sql_query_str = create_sql_query(form_data)
	database = 'db.sqlite3'
	connection = create_connection(database)
	cursor = connection.cursor()
	current = cursor.execute(sql_query_str,
	{
	'value1':form_data['structure_type'],
	'value2':form_data['building_material'],
	'value3':form_data['service'],
	'value4':form_data['construction_operation']
	})
	fetched_data = current.fetchall()
	return fetched_data

def create_connection(db_file):
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as err:
		print(err)

	return None