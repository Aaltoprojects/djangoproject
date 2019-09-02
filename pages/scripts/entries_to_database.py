import datetime
import pages.constants as constants
from pages.models import Project

def add_entries():
	count = 0
	for destination_type in constants.STRUCTURE_TYPES:
		for building_mat in constants.BUILDING_MATERIALS:
			for srvc in constants.SERVICES:
				for construction_oper in constants.CONSTRUCTION_OPERATIONS:
					description = (str(destination_type[1]) + ' ' + str(building_mat[1]) + ' ' + str(srvc[1]) + ' ' + str(construction_oper[1]))
					print(description)
					instance = Project(
						project_name = 'Projekti ' + str(count),
						destination_name = 'Kohde ' + str(count),
						start_date = datetime.date.today(),
						end_date = datetime.date.today(),
						structure_type = destination_type[0],
						building_material = building_mat[0],
						service = srvc[0],
						construction_operation = construction_oper[0],
						specific_project_type = description,
						project_description = '',
						documentation_path = 'Esimerkki/Kansio ' + str(count),
						project_manager = 'Projektin vetäjä ' + str(count)
						)
					instance.save()
					count += 1