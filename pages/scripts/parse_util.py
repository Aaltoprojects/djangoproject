import pages.constants as constants
from pages.models import Filter
from openpyxl import Workbook
import datetime as dt
from pages.constants import DATE_FORMAT


def format_qset(data_qs):
    array = []
    for filter in data_qs:
        name = filter.filter_name
        array.append(name)
    return array


def filters_qs_to_dict(filters_qs):
    values = filters_qs.values()
    filters_dict = {}
    for filter in constants.FILTER_CATEGORY_NAMES:
        filters_dict[filter] = []
    for d in values:
        category = d['category']
        filter_name = d['filter_name']
        filters_dict[category].append(filter_name)
    return filters_dict


def parse_input_filters(data):
    chosen_filters = []
    chosen_filters += data.getlist('structure_type')
    chosen_filters += data.getlist('building_material')
    chosen_filters += data.getlist('service')
    chosen_filters += data.getlist('construction_operation')
    chosen_filters += data.getlist('structural_component')
    filter_objs = Filter.filter_db.filter(filter_name__in=chosen_filters)
    return filter_objs

def format_time(time):
  return dt.datetime.strptime(str(time),'%Y-%m-%d').strftime(DATE_FORMAT) if time is not None else time