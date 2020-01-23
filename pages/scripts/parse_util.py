import pages.constants as constants
from pages.models import Filter
from openpyxl import Workbook

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

def write_to_excel(result, response):
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = 'Tuloste'
    columns = [
        'Projektin nimi',
        'Kohteen nimi',
        'Aloituspäivämäärä',
        'Lopetuspäivämäärä',
        'Avainsanat',
        'Projektin kuvaus',
        'Polku tiedostojen sijaintiin',
        'Projektipäällikkö',
    ]
    row_num = 1
    for col_num, column_title in enumerate(columns, 1):
        cell = worksheet.cell(row=row_num, column=col_num)
        cell.value = column_title
    for project in result:
        row_num += 1
        row = [
            project.project_name,
            project.destination_name,
            project.start_date,
            project.end_date,
            project.keywords,
            project.project_description,
            project.documentation_path,
            project.project_manager,
        ]
        for col_num, cell_value in enumerate(row, 1):
            cell = worksheet.cell(row=row_num, column=col_num)
            cell.value = cell_value
    workbook.save(response)