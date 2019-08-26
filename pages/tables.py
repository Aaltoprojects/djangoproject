import django_tables2 as tables
from .models import Project
import pages.constants as constants

class SearchResultTable(tables.Table):
	class Meta:
		model = Project
		template_name = constants.DJANGO_TABLES2_TEMPLATE