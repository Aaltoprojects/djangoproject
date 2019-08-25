from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Project(models.Model):
	project_db = models.Manager()

	project_name = models.CharField(max_length=200)
	destination_name = models.CharField(max_length=200)
	start_date = models.DateField(null=True)
	end_date = models.DateField(null=True)
	#4 Structure types, but keep more until confirmed
	#Asuin-, Liike-, Teollisuus-, Geokohde
	structure_type = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)])
	#6 Building materials, but keep more until confirmed
	#Puu, Betoni, Teräs, Tiili, Lasi, Kivi
	building_material = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)])
	#Is this field relevant? Need confirmation
	#Suunnittelu, Tutkimus, jne.
	service = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)])
	#Can make service field obselete
	#Korjaaminen, Uusiminen, Täydentäminen, Korottaminen
	construction_operation = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)])
	#These types are listed from the Excel and are not defined by user
	specific_project_type = models.CharField(null=True,default=None,max_length=200)
	project_description = models.CharField(null=True,default=None,max_length=500)
	documentation_path = models.CharField(null=True,default=None,max_length=200)
	#Currently registers project manager only, but in the future will include all employees
	project_manager = models.CharField(null=True,default=None,max_length=100)

	def __str__(self):
		return self.project_name