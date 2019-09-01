import django_tables2 as tables
from django_tables2 import TemplateColumn
import pages.models as models

class SearchResultTable(tables.Table):
	class Meta:
		model = models.Project
		attrs = {'class': 'table table-bordered'}
	Muokkaa = TemplateColumn(template_name = 'snippets/edit_button.html')