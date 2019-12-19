import datetime as dt
from pages.models import Project, Filter
from django.db.models import Q
import pages.constants as constants
from pages.scripts.parse_util import format_qset, parse_input_filters
from pages.constants import FILTER_CATEGORY_NAMES


def get_filters():
    return tuple(format_qset(Filter.filter_db.filter(category=filter)) for filter in FILTER_CATEGORY_NAMES)


def sql_query(data_dict):
    temp1 = str(data_dict.getlist('start_date')[0])
    temp2 = str(data_dict.getlist('end_date')[0])
    temp3 = str(data_dict.getlist('key_phrase_search')[0])
    filter_names = []
    data_qs = Project.project_db.all()

    if 'structure_type' in data_dict:
        filter_names += data_dict.getlist('structure_type')
    if 'building_material' in data_dict:
        filter_names += data_dict.getlist('building_material')
    if 'service' in data_dict:
        filter_names += data_dict.getlist('service')
    if 'construction_operation' in data_dict:
        filter_names += data_dict.getlist('construction_operation')
    if 'structural_component' in data_dict:
        filter_names += data_dict.getlist('structural_component')

    if filter_names:
        filter_qs = Filter.filter_db.filter(filter_name__in=filter_names)
        data_qs = data_qs.filter(filters__in=filter_qs)

    if temp1 != '':
        temp1 = str(dt.datetime.strptime(temp1,'%d.%m.%Y').strftime('%Y-%m-%d'))
        data_qs = data_qs.filter(end_date__range=[temp1, '2100-01-01'])
    if temp2 != '':
        temp2 = str(dt.datetime.strptime(temp2,'%d.%m.%Y').strftime('%Y-%m-%d'))
        data_qs = data_qs.filter(start_date__range=['1970-01-01', temp2])
    if temp3 != '':
        qset = Q()
        for term in temp3.split():
            tmp = Q()
            tmp |= Q(project_name__icontains=term)
            tmp |= Q(destination_name__icontains=term)
            tmp |= Q(keywords__icontains=term)
            tmp |= Q(project_description__icontains=term)
            tmp |= Q(documentation_path__icontains=term)
            tmp |= Q(project_manager__icontains=term)
            qset &= tmp
        data_qs = data_qs.filter(qset)

    return data_qs


def search(data_dict):
    data_qs = sql_query(data_dict)
    return data_qs

def save_entry_to_db(form, input_data):
    input_filters = parse_input_filters(input_data)
    obj = Project(
                project_name=form.cleaned_data['project_name'],
                destination_name=form.cleaned_data['destination_name'],
                start_date=form.cleaned_data['start_date'],
                end_date=form.cleaned_data['end_date'],
                keywords=form.cleaned_data['keywords'],
                project_description=form.cleaned_data['project_description'],
                documentation_path=form.cleaned_data['documentation_path'],
                project_manager=form.cleaned_data['project_manager'],
                )
    obj.save()
    for input_filter in input_filters:
        obj.filters.add(input_filter)

def edit_entry_in_db(project, form, input_data):
    input_filters = parse_input_filters(input_data)
    project.project_name = form.cleaned_data['project_name']
    project.destination_name = form.cleaned_data['destination_name']
    project.start_date = form.cleaned_data['start_date']
    project.end_date = form.cleaned_data['end_date']
    project.keywords = form.cleaned_data['keywords']
    project.project_description = form.cleaned_data['project_description']
    project.documentation_path = form.cleaned_data['documentation_path']
    project.project_manager = form.cleaned_data['project_manager']
    project.save()
    project.filters.clear()
    for input_filter in input_filters:
        project.filters.add(input_filter)

def check_if_exists_in_db(add_filter_form):
    input_category = add_filter_form.cleaned_data['category']
    input_name = add_filter_form.cleaned_data['filter_name']
    matching_qs = Filter.filter_db.filter(category=input_category,
                                            filter_name__iexact=input_name,
                                            )
    return matching_qs