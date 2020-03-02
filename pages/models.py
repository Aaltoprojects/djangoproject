from django.db import models
import pages.constants as constants

class Filter(models.Model):

	filter_db = models.Manager()

	category = models.CharField(
		max_length=200,
		verbose_name='Filtterikategoria',
		choices=constants.FILTER_CATEGORIES,
		)
	filter_name = models.CharField(
		max_length=200,
		verbose_name='Filtteri',
		)

	def __str__(self):
		return self.filter_name

class Project(models.Model):

	project_db = models.Manager()

	project_name = models.CharField(
		max_length=200,
		verbose_name='Projektin nimi',
		)
	destination_name = models.CharField(
		max_length=200,
		verbose_name='Kohteen nimi',
		)
	start_date = models.DateField(
		null=True,
		verbose_name='Aloituspäivämäärä',
		)
	end_date = models.DateField(
		null=True,
		verbose_name='Lopetuspäivämäärä',
		)
	keywords = models.CharField(
		null=True,
		max_length=200,
		verbose_name='Avainsanat',
		)
	project_description = models.CharField(
		null=True,
		max_length=10000,
		verbose_name='Projektin kuvaus',
		)
	documentation_path = models.CharField(
		null=True,
		max_length=500,
		verbose_name='Polku tiedostojen sijaintiin',
		)
	project_manager = models.CharField(
		null=True,
		max_length=100,
		verbose_name='Projektipäällikkö',
		)
	filters = models.ManyToManyField(Filter)

	def __str__(self):
		return self.project_name

class ReferenceProject(models.Model):

	project = models.OneToOneField(
		Project,
		on_delete=models.CASCADE,
		primary_key=True,
		)

	undertaking = models.CharField(
		null=True,
		max_length=200,
		verbose_name='Hanke',
		)

	client = models.CharField(
		null=True,
		max_length=200,
		verbose_name='Tilaaja',
		)

	area = models.FloatField(
		null=True,
		verbose_name='Laajuus (brm2)',
		)

	construction_cost = models.FloatField(
		null=True,
		verbose_name='Rakentamiskustannukset',
		)

	project_accepted = models.DateField(
		null=True,
		verbose_name='Hanke vastaanotettu',
		)

	construction_permit_granted = models.DateField(
		null=True,
		verbose_name='Rakennuslupa myönnetty',
		)

	def __str__(self):
		return self.project.project_name


