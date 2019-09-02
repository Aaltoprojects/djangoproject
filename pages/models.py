from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Project(models.Model):
	project_db = models.Manager()
	project_name = models.CharField(max_length=200, verbose_name='Projektin nimi')
	destination_name = models.CharField(max_length=200, verbose_name='Kohteen nimi')
	start_date = models.DateField(null=True, verbose_name='Aloituspäivämäärä')
	end_date = models.DateField(null=True, verbose_name='Lopetuspäivämäärä')
	structure_type = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)], verbose_name='Rakennustyyppi')
	building_material = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)], verbose_name='Rakennusmateriaali')
	#relevant field? Confirm.
	service = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)], verbose_name='Palvelu')
	construction_operation = models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)], verbose_name='Rakennustoimenpide')
	specific_project_type = models.CharField(null=True,default=None,max_length=200, verbose_name='Osaamisalue')
	project_description = models.CharField(null=True,default=None,max_length=500, verbose_name='Projektin kuvaus')
	documentation_path = models.CharField(null=True,default=None,max_length=200, verbose_name='Polku tiedostojen sijaintiin')
	project_manager = models.CharField(null=True,default=None,max_length=100, verbose_name='Projektin vetäjä')

	def __str__(self):
		return self.project_name