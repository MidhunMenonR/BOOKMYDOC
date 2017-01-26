from django.shortcuts import render
from django.conf import settings
from .models import DocDetails
from .models import Locations
# Create your views here.

def home(request):
	return render(request,'index.html')


def prof(request):

	model = DocDetails 
	modelobj = DocDetails.objects.get(doc_username='vinod')
	context ={
		"title" : "Doctor",
		"model" : modelobj
	}

	
	return render(request,'docdetails.html',context)


def loginPage(request):
	return render(request,'login.html',{})


def loginform(request):
	data = request.POST
	print 'USERNAME: ' +data['usrnm']
	print 'pASSWORD '+ data['pwd']
	
	
	value = 0
	usr = DocDetails.objects.get(doc_username=  data['usrnm'])
	locs = Locations.objects.filter(doc_id = usr.doc_username )

	context ={
		"title" : "Doctor",
		"model" : usr,
		"locations" : locs
	}
	if usr.doc_password == data['pwd'] :
		value = 1
		print 'passed'
		print usr.pk
		for l in locs :
			print l.location

	if value == 1:
		return render(request,'docdetails.html',context)

	else :	
		return render(request,'login.html',{})

def searchform(request):
	data = request.GET
	print 'name' + data['srchname']
	print 'loc' + data['srchloc']
	print 'dept' + data['srchdept']
	return render(request,'searchpage.html')

