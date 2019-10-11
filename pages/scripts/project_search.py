from pages.models import Project
from django.db.models import Q
import pages.constants as constants

def sql_query(form_data):
	data_qs = Project.project_db.all()
	temp1 = str(form_data['start_date'])
	temp2 = str(form_data['end_date'])
	temp3 = str(form_data['structure_type'])
	temp4 = str(form_data['building_material'])
	temp5 = str(form_data['service'])
	temp6 = str(form_data['construction_operation'])
	temp7 = str(form_data['key_phrase_search'])
	if temp1 != 'None':
		data_qs = data_qs.filter(end_date__range = [temp1, '2100-01-01'])
	if temp2 != 'None':
		data_qs = data_qs.filter(start_date__range = ['1970-01-01', temp2])
	if temp3 != constants.default_entry[0]:
		data_qs = data_qs.filter(structure_type = temp3)
	if temp4 != constants.default_entry[0]:
		data_qs = data_qs.filter(building_material = temp4)
	if temp5 != constants.default_entry[0]:
		data_qs = data_qs.filter(service = temp5)
	if temp6 != constants.default_entry[0]:
		data_qs = data_qs.filter(construction_operation = temp6)
	if temp7 != '':
		qset = Q()
		for term in temp7.split():
			tmp = Q()
			tmp |= Q(project_name__contains=term)
			tmp |= Q(destination_name__contains=term)
			tmp |= Q(structure_type__contains=term)
			tmp |= Q(building_material__contains=term)
			tmp |= Q(service__contains=term)
			tmp |= Q(construction_operation__contains=term)
			tmp |= Q(keywords__contains=term)
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
	'key_phrase_search': form.cleaned_data['key_phrase_search']
	}
	data_qs = sql_query(form_data)
	return data_qs