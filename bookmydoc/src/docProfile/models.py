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
	location = models.CharField(max_length=50,unique = True)
	def __unicode__(self):
		return self.location	

class BookDoc(models.Model) :
	loc_id = models.ForeignKey(Locations) 
	address = models.CharField(max_length=200)
	start_time = models.CharField(max_length=5)
	end_time = models.CharField(max_length=5)
	duration = models.IntegerField()
	def __unicode__(self):
		return self.address

class BookDetails(models.Model) :
	doc_name = models.CharField(max_length=20)
	location = models.CharField(max_length=50)
	time_slot = models.CharField(max_length=5)
	def __unicode__(self):
		return self.doc_name