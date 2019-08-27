default_entry = (0, '—')

STRUCTURE_TYPES = [
	default_entry,
	(1, 'Asuinrakennus'),
	(2, 'Liikerakennukset'),
	(3, 'Teollisuusrakennukset'),
	(4, 'Georakennukset')
]

BUILDING_MATERIALS = [
	default_entry,
	(1, 'Puu'),
	(2, 'Betoni'),
	(3, 'Teräs'),
	(4, 'Tiili'),
	(5, 'Lasi'),
	(6, 'Kivi')
]

SERVICES = [
	default_entry,
	(1, 'Suunnittelu'),
	(2, 'Tutkimus')
]

CONSTRUCTION_OPERATIONS = [
	default_entry,
	(1, 'Korjaaminen'),
	(2, 'Uusiminen'),
	(3, 'Täydentäminen'),
	(4, 'Korottaminen')
]

YEARS = range(2010,2024)

ELEMS_DICT = {
		'structure_type': ':value1',
 		'building_material': ':value2',
 		'service': ':value3',
 		'construction_operation': ':value4'
		}

DJANGO_TABLES2_TEMPLATE = 'django_tables2/bootstrap4.html'