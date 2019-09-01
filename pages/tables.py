import django_tables2 as tables
from django_tables2 import TemplateColumn
import pages.models as models

class SearchResultTable(tables.Table):
	Lisätiedot = TemplateColumn(template_name = 'snippets/edit_button.html')
	class Meta:
		model = models.Project
		fields = (
			'project_name',
			'destination_name',
			'start_date',
			'end_date',
			'structure_type',
			'building_material',
			'service',
			'construction_operation',
			'specific_project_type',
			)
		empty_text = 'Ei tuloksia'
		show_header = True
		attrs = {'class': 'table table-bordered'}