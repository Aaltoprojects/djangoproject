from pages.models import Filter
from django.db.models import Q
import pages.constants as constants

def fetch_all():
	data_qs = Filter.filter_db.all()
	f1 = data_qs.filter(category = 'Rakennustyyppi')
	f2 = data_qs.filter(category = 'Rakennusmateriaali')
	f3 = data_qs.filter(category = 'Palvelu')
	f4 = data_qs.filter(category = 'Rakennustoimenpide')
	f5 = data_qs.filter(category = 'Rakenneosa')
	return f1, f2, f3, f4, f5