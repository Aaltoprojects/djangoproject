from django.db import models

'''
class employees(models.Model):
	name = models.CharField(max_length = 30, default=None)
	surname = models.CharField(max_length = 30, default=None)
	pnumber = models.CharField(max_length = 30, default=None)
	email = models.CharField(max_length = 30, default=None)
	title = models.CharField(max_length = 30, default=None)
	function = models.CharField(max_length = 30, default=None)

	siivous = models.IntegerField(default=None)
	tetsaus = models.IntegerField(default=None)
	johtaminen = models.IntegerField(default=None)

	def __str__(self):
		return self.name + ' ' + self.surname
'''

class osaamisalue(models.Model):
	nimi = models.CharField(max_length = 200, default = None)
	rakennustyyppi = models.IntegerField(default = None)
	rakennusmateriaali = models.IntegerField(default = None)
	palvelu = models.IntegerField(default = None)
	rakennutoimenpide = models.IntegerField(default = None)

	def __str__(self):
		return self.nimi

class projektit(models.Model):
	nimi = models.CharField(max_length = 200, default = None)
	rakennustyyppi = models.IntegerField(default = None)
	rakennusmateriaali = models.IntegerField(default = None)
	palvelu = models.IntegerField(default = None)
	rakennutoimenpide = models.IntegerField(default = None)
	vapaa_kuvaus = models.CharField(max_length = 5000, default = None)
	linkki_dokumentteihin = models.CharField(max_length = 200, default = None)
	projektihenkilot = models.CharField(max_length = 1000, default = None)

	def __str__(self):
		return self.nimi