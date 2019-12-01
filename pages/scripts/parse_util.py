import pages.constants as constants
from pages.models import Filter

def format_qset(data_qs):
        array = []
        for filter in data_qs:
            name = filter.filter_name
            array.append(name)
        return array

def parse_input_filters(data):
	chosen_filters = []
	chosen_filters += data.getlist('structure_type')
	chosen_filters += data.getlist('building_material')
	chosen_filters += data.getlist('service')
	chosen_filters += data.getlist('construction_operation')
	chosen_filters += data.getlist('structural_component')
	filter_objs = Filter.filter_db.filter(filter_name__in = chosen_filters)
	return filter_objs