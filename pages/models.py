from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Project(models.Model):
	project_db = models.Manager()
	project_name = models.CharField(max_length=200, verbose_name="Projektin nimi")
	destination_name = models.CharField(max_length=200, verbose_name="Kohteen nimi")
	start_date = models.DateField(null=True, verbose_name="Aloituspäivämäärä")
	end_date = models.DateField(null=True, verbose_name="Lopetuspäivämäärä")
	#4 Structure types, but keep more until confirmed
	#Asuin-, Liike-, Teollisuus-, Geokohde
	structure_type = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)], verbose_name="Rakennustyyppi")
	#6 Building materials, but keep more until confirmed
	#Puu, Betoni, Teräs, Tiili, Lasi, Kivi
	building_material = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)], verbose_name="Rakennusmateriaali")
	#Is this field relevant? Need confirmation
	#Suunnittelu, Tutkimus, jne.
	service = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)], verbose_name="Palvelu")
	#Can make service field obselete
	#Korjaaminen, Uusiminen, Täydentäminen, Korottaminen
	construction_operation = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)], verbose_name="Rakennustoimenpide")
	#These types are listed from the Excel and are not defined by user
	specific_project_type = models.CharField(null=True,default=None,max_length=200, verbose_name="Osaamisalue")
	project_description = models.CharField(null=True,default=None,max_length=500, verbose_name="Projektin kuvaus")
	documentation_path = models.CharField(null=True,default=None,max_length=200, verbose_name="Polku tiedostojen sijaintiin")
	#Currently registers project manager only, but in the future will include all employees
	project_manager = models.CharField(null=True,default=None,max_length=100, verbose_name="Projektin vetäjä")

	def __str__(self):
		return self.project_name