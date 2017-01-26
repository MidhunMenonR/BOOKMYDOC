from django.db import models

# Create your models here.

class DocDetails(models.Model) :
	doc_username = models.CharField(max_length=20,primary_key =True,unique = True)
	doc_password = models.CharField(max_length=20)
	doc_name =  models.CharField(max_length=50)
	doc_location = models.CharField(max_length=50)
	doc_phone = models.CharField(max_length=13)
	doc_department = models.CharField(max_length=20)
	


	def __unicode__(self):
		return self.doc_username
class Locations(models.Model) :
	doc_id = models.ForeignKey(DocDetails)
	location = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.location	