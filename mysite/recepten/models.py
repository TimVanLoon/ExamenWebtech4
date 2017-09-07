from django.db import models

class Recept(models.Model):
	recept_naam = models.CharField(max_length=50)
	recept_calorieAantal = models.CharField(max_length=50)
	recept_ingredient= models.CharField(max_length=50)
	recept_benodigdeTijd = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.recept_naam

