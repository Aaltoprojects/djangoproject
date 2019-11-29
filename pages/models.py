from django.db import models
import pages.constants as constants

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
		max_length=1000,
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
		verbose_name='Projektin vetäjä',
		)
	filters = models.ManyToManyField(Filter)

	def __str__(self):
		return self.project_name

class Filter(models.Model):

	filter_db = models.Manager()

	category = models.CharField(
		max_length=200,
		verbose_name='Filtterikategoria',
		widget=forms.Select(choices=constants.FILTER_CATEGORIES),
		)
	filter_name = models.CharField(
		max_length=200,
		verbose_name='Filtteri',
		)

	def __str__(self):
		return self.filter_name