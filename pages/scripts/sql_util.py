import datetime as dt
from pages.models import Project, Filter, ReferenceProject
from django.db.models import Q
import pages.constants as constants
from pages.scripts.parse_util import format_qset, parse_input_filters
from pages.constants import FILTER_CATEGORY_NAMES


def get_filters():
    filters = {str(filter):format_qset(Filter.filter_db.filter(category=filter)) for filter in FILTER_CATEGORY_NAMES}
    return filters

def is_reference_search(data_dict):
    if 'is_ref' in data_dict:
        return True
    else:
        return False

def sql_query(data_dict):
    start_date = str(data_dict.getlist('start_date')[0])
    end_date = str(data_dict.getlist('end_date')[0])
    key_phrases = str(data_dict.getlist('key_phrase_search')[0])
    filter_names = []
    projects = Project.project_db.all()

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
        projects = projects.filter(filters__in=filter_qs)

    if start_date != '':
        start_date = str(dt.datetime.strptime(start_date,'%d.%m.%Y').strftime('%Y-%m-%d'))
        projects = projects.filter(end_date__range=[start_date, '2100-01-01'])
    if end_date != '':
        end_date = str(dt.datetime.strptime(end_date,'%d.%m.%Y').strftime('%Y-%m-%d'))
        projects = projects.filter(start_date__range=['1970-01-01', end_date])
    if is_reference_search(data_dict):
        references = ReferenceProject.objects.all()
        if str(data_dict.getlist('area')[0]) != '':
            area = float(data_dict.getlist('area')[0])
            references = references.filter(area__range=[area, 10000000])
        projects = projects.filter(referenceproject__in=references)
    if key_phrases != '':
        qset1 = Q()
        qset2 = Q()
        for term in key_phrases.split():
            tmp1 = Q()
            tmp1 |= Q(project_name__icontains=term)
            tmp1 |= Q(destination_name__icontains=term)
            tmp1 |= Q(keywords__icontains=term)
            tmp1 |= Q(project_description__icontains=term)
            tmp1 |= Q(documentation_path__icontains=term)
            tmp1 |= Q(project_manager__icontains=term)
            qset1 &= tmp1
            tmp2 = Q()
            tmp2 |= Q(undertaking__icontains=term)
            tmp2 |= Q(client__icontains=term)
            qset2 &= tmp2
        p1 = projects.filter(qset1)
        p2 = ReferenceProject.objects.all().filter(qset2)
        p3 = projects.filter(referenceproject__in=p2)
        projects = p1.union(p3)
    return projects.distinct()

def search(data_dict):
    projects = sql_query(data_dict)
    return projects

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
    return obj

def save_ref_to_db(form, input_project):
    obj = ReferenceProject(
                project=input_project,
                undertaking=form.cleaned_data['undertaking'],
                client=form.cleaned_data['client'],
                area=form.cleaned_data['area'],
                construction_cost=form.cleaned_data['construction_cost'],
                project_accepted=form.cleaned_data['project_accepted'],
                construction_permit_granted=form.cleaned_data['construction_permit_granted'],
                )
    obj.save()
    return obj

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

def edit_ref_in_db(reference_project, form):
    reference_project.undertaking = form.cleaned_data['undertaking']
    reference_project.client = form.cleaned_data['client']
    reference_project.area = form.cleaned_data['area']
    reference_project.construction_cost = form.cleaned_data['construction_cost']
    reference_project.project_accepted = form.cleaned_data['project_accepted']
    reference_project.construction_permit_granted = form.cleaned_data['construction_permit_granted']
    reference_project.save()

def check_if_exists_in_db(add_filter_form):
    input_category = add_filter_form.cleaned_data['category']
    input_name = add_filter_form.cleaned_data['filter_name']
    matching_qs = Filter.filter_db.filter(category=input_category,
                                            filter_name__iexact=input_name,
                                            )
    return matching_qs