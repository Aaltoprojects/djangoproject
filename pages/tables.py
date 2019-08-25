import django_tables2 as tables
from .models import Project

class SearchResultTable(tables.Table):
	class Meta:
		model = Project
		template_name = 'django_tables2/bootstrap.html'