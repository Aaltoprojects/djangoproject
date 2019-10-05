default_entry = ('—', '—')
YEARS = range(2010,2024)
DATE_FORMAT = '%d.%m.%Y'

STRUCTURE_TYPES = [
	default_entry,
	('Asuinrakennus', 'Asuinrakennus'),
	('Liikerakennukset', 'Liikerakennukset'),
	('Teollisuusrakennukset', 'Teollisuusrakennukset'),
	('Georakennukset', 'Georakennukset')
]

BUILDING_MATERIALS = [
	default_entry,
	('Puu', 'Puu'),
	('Betoni', 'Betoni'),
	('Teräs', 'Teräs'),
	('Tiili', 'Tiili'),
	('Lasi', 'Lasi'),
	('Kivi', 'Kivi')
]

SERVICES = [
	default_entry,
	('Suunnittelu', 'Suunnittelu'),
	('Tutkimus', 'Tutkimus')
]

CONSTRUCTION_OPERATIONS = [
	default_entry,
	('Korjaaminen', 'Korjaaminen'),
	('Uusiminen', 'Uusiminen'),
	('Täydentäminen', 'Täydentäminen'),
	('Korottaminen', 'Korottaminen')
]