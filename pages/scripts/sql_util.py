from pages.models import Project, Filter
from django.db.models import Q
import pages.constants as constants
from pages.scripts.parse_util import format_qset


def get_filters():
    f1 = format_qset(Filter.filter_db.filter(category='Rakennustyyppi'))
    f2 = format_qset(Filter.filter_db.filter(category='Rakennusmateriaali'))
    f3 = format_qset(Filter.filter_db.filter(category='Palvelu'))
    f4 = format_qset(Filter.filter_db.filter(category='Rakennustoimenpide'))
    f5 = format_qset(Filter.filter_db.filter(category='Rakenneosa'))
    return f1, f2, f3, f4, f5


def sql_query(form, data_dict):
    temp1 = str(form.cleaned_data['start_date'])
    temp2 = str(form.cleaned_data['end_date'])
    temp3 = str(form.cleaned_data['key_phrase_search'])
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

    if temp1 != 'None':
        data_qs = data_qs.filter(end_date__range=[temp1, '2100-01-01'])
    if temp2 != 'None':
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


def search(form, data_dict):
    data_qs = sql_query(form, data_dict)
    return data_qs
