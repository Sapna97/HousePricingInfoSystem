from django.db import models

# Create your models here.
class Parameters(models.Model):
	area_type =  models.CharField(max_length=200)
	location =   models.CharField(max_length=200)
	bedrooms =   models.IntegerField()
	hallkichen = models.IntegerField()
	area_sqft =  models.IntegerField()
	bathrooms =  models.IntegerField()
	balconies =  models.IntegerField()

	def __str__(self):
		return self.area_type


