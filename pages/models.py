from django.db import models

class employees(models.Model):
	name = models.CharField(max_length = 30)
	surname = models.CharField(max_length = 30)
	title = models.CharField(max_length = 60)
	function = models.CharField(max_length = 30)
	
	siivous = models.IntegerField()
	tetsaus = models.IntegerField()
	johtaminen = models.IntegerField()

	def __str__(self):
		return self.name + ' ' + self.surname