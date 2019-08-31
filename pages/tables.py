import django_tables2 as tables
from django_tables2 import TemplateColumn
from .models import Project

class SearchResultTable(tables.Table):
	class Meta:
		model = Project
		attrs = {'class': 'table table-bordered'}
	Muokkaa = TemplateColumn(template_name = 'snippets/edit_button.html')