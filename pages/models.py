from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class project(models.Model):
	project_name = models.CharField(max_length = 200, default = None)
	destination = models.CharField(max_length = 200, default = None)
	start_date = models.DateField()
	end_date = models.DateField()

	#4 Structure types, but keep more until confirmed
	#Asuin-, Liike-, Teollisuus-, Geokohde
	destination_type = models.IntegerField(default = None, validators=[MaxValueValidator(10), MinValueValidator(1)])

	#6 Building materials, but keep more until confirmed
	#Puu, Betoni, Teräs, Tiili, Lasi, Kivi
	building_material = models.IntegerField(default = None, validators=[MaxValueValidator(10), MinValueValidator(1)])

	#Is this field relevant? Need confirmation
	#Suunnittelu, Tutkimus, jne.
	service = models.IntegerField(default = None, validators=[MaxValueValidator(10), MinValueValidator(1)])

	#Can make service field obselete
	#Korjaaminen, Uusiminen, Täydentäminen, Korottaminen
	contruction_operation = models.IntegerField(default = None, validators=[MaxValueValidator(10), MinValueValidator(1)])

	#These types are listed from the Excel and are not defined by user
	specific_project_type = models.CharField(max_length = 200, default = None)

	project_description = models.CharField(max_length = 500, default = None)
	documentation_path = models.CharField(max_length = 200, default = None)

	#Currently registers project manager only, but in the future will include all employees
	project_manager = models.CharField(max_length = 100, default = None)

	def __str__(self):
		return self.project_name