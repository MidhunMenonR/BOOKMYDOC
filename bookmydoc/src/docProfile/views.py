from django.shortcuts import render
from django.conf import settings
from .models import DocDetails
from .models import Locations
from .models import BookDoc
from .models import BookDetails
import datetime
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
	locdets = []
	locaddresses = []
	usr = DocDetails.objects.get(doc_username=  data['usrnm'])
	locs = Locations.objects.filter(doc_id = usr.doc_username )
	#adding details of each location for different days
	for l  in locs :
		locationdetail = BookDoc.objects.filter(loc_id = l.id)
		for ld in locationdetail :
			
			locdets.append(ld)


	context ={
		"title" : "Doctor",
		"model" : usr,
		"locations" : locs,
		"locationdetails" : locdets
	}
	if usr.doc_password == data['pwd'] :
		value = 1
		print 'passed'
		print usr.pk
		for l in locs :
			print l.location
			print l.id
		print locdets

	if value == 1:
		return render(request,'Doc-edit.html',context)

	else :	
		return render(request,'login.html',{})

def searchform(request):
	data = request.GET
	print 'name' + data['srchname']
	print 'loc' + data['srchloc']
	print 'dept' + data['srchdept']
	docobjectlist = []


	if data['srchloc'] :
		tloclist = []
		slocations = Locations.objects.filter(area__icontains  = data['srchloc'])
		for sl in slocations:
			doctor = DocDetails.objects.get(doc_username = sl.doc_id)
			tloclist.append(doctor)
		tloclist = list(set(tloclist))
		if data['srchname'] :
			tnamlist = []
			for tl in tloclist :
				if data['srchname'] in tl.doc_name.lower() :
					tnamlist.append(tl)
			if data['srchdept']	:
				for tn in tnamlist :
					if data['srchdept'] in tn.doc_department.lower() :
						docobjectlist.append(tn)
			else :
				for tn in tnamlist :
					docobjectlist.append(tn)

		elif data['srchdept']:
			for tl in tloclist :
					if data['srchdept'] in tl.doc_department.lower() :
						docobjectlist.append(tl)
		else :
			docobjectlist = tloclist
	elif data['srchdept'] :
		doctor = DocDetails.objects.filter(doc_department__icontains = data['srchdept'] )	
		if data['srchname'] :
			for d in doctor :
				if 	data['srchname'] in d.doc_name.lower() :
					docobjectlist.append(d)
		else :
			docobjectlist = doctor
	elif data['srchname'] :
		docobjectlist = DocDetails.objects.filter(doc_name__icontains = data['srchname'])
									
	
	for d in docobjectlist:
		print d.doc_name
		print d.doc_phone

	context = {
		"doctorslist" : docobjectlist

	}



	return render(request,'searchpage.html',context)


def docdetails(request):
	data = request.GET
	localist = []
	date_list = []
	dayonetime_list = []
	daytwotime_list = []
	daythreetime_list = []



	i=0
	
	date_list.append(datetime.date.today())
	date_list.append(datetime.date.today() + datetime.timedelta(days=1))
	date_list.append(datetime.date.today() + datetime.timedelta(days=2))
	
	

	doc = DocDetails.objects.get(doc_username = data['docusername'])
	loc = Locations.objects.filter(doc_id = doc.doc_username )


	#creating list of locations of doctor
	for l in loc :
		locdet = BookDoc.objects.filter(loc_id = l.id)
		localist += locdet
	now = datetime.datetime.now().strftime('%H:%M:%S')
	nhh = now.split(":")
	nmm = int(nhh[1])
	nhh = int(nhh[0])


	for d in localist :
		datecheck = str(datetime.date.today() )
		#checking whether doctor is available
		datecyear = str(date_list[0])
		datecyear = datecyear.split("-")
		datecday = int(datecyear[0])
		datecmonth = int(datecyear[1])
		datecyear = int(datecyear[2])
		print "printing..."
		
		datelyear = d.date.split("-")
		datelday = int(datelyear[0])
		datelmonth = int(datelyear[1])
		datelyear = int(datelyear[2])
		
		

		if((datecyear == datelyear) and (datecmonth == datelmonth) and (datecday == datelday)) :
			print "datematch"


			shh = d.start_time.split(":")
			curtime_list = []
			
			
			
			smm = int(shh[1])
			shh = int(shh[0])
			

			ehh = d.end_time.split(":")
			
			emm = int(ehh[1])
			ehh = int(ehh[0])
			
			

			chh=shh
			cmm=smm
			datecheck = str(datetime.date.today() )

		
			while(chh<ehh) :

				
				flag = 1 #for addind to timelist
				if nhh >= chh :
					flag = 0
				elif (chh-1) == nhh :
					if (cmm-nmm)<0 :
						flag = 0 
						


				if(chh==12):
					ctime=str(chh)+':'+str(cmm)+" "+'PM'

				elif( chh<12):
					ctime=str(chh)+':'+str(cmm)+" "+'AM'
				else :
					thh=(chh%12)
					ctime=str(thh)+':'+str(cmm)+" "+'PM'
				
				# searching in bookdetails
				if flag != 0 :
					searchtable =  BookDetails.objects.filter(doc_name = data['docusername'])
					
					for s in searchtable :
						if s.date == datecheck:
							if s.doc_name == doc.doc_username :
								for n in loc : 
									if n.location == s.location :
										if s.time_slot == ctime :
											flag = 0

									

				if flag == 1 :
					curtime_list.append(ctime)
				cmm += d.duration
				if(cmm >= 60):
					if(chh < 23) :
						chh+=1	
						cmm=cmm%60
					else :
						break
			dayonetime_list.append(curtime_list)			


		#checking whether doctor is available
		datecyear = str(date_list[1])
		datecyear = datecyear.split("-")
		datecday = int(datecyear[0])
		datecmonth = int(datecyear[1])
		datecyear = int(datecyear[2])
		print "printing..."
		
		datelyear = d.date.split("-")
		datelday = int(datelyear[0])
		datelmonth = int(datelyear[1])
		datelyear = int(datelyear[2])
		
		

		if((datecyear == datelyear) and (datecmonth == datelmonth) and (datecday == datelday)) :
			print "datematch"	

			shh = d.start_time.split(":")
			curtime_list = []
			
			
			
			smm = int(shh[1])
			shh = int(shh[0])
			

			ehh = d.end_time.split(":")
			
			emm = int(ehh[1])
			ehh = int(ehh[0])
			
			

			chh=shh
			cmm=smm			
				
				
			
			datecheck = str(datetime.date.today()+datetime.timedelta(days=1) )
			



			while(chh<ehh) :

				flag = 1 #for addind to timelist

				if(chh==12):
					ctime=str(chh)+':'+str(cmm)+" "+'PM'

				elif( chh<12):
					ctime=str(chh)+':'+str(cmm)+" "+'AM'
				else :
					thh=(chh%12)
					ctime=str(thh)+':'+str(cmm)+" "+'PM'
				
				# searching in bookdetails
				searchtable =  BookDetails.objects.filter(doc_name = data['docusername'])
				for s in searchtable :
					if s.date == datecheck:
						if s.doc_name == doc.doc_username :
							for n in loc : 
								if n.location == s.location :
									if s.time_slot == ctime :
										flag = 0

								
				if flag == 1 :
					curtime_list.append(ctime)
				cmm += d.duration
				if(cmm >= 60):
					if(chh < 23) :
						chh+=1	
						cmm=cmm%60
					else :
						break
				
				
				
				
				
			



			daytwotime_list.append(curtime_list)

		datecyear = str(date_list[2])
		datecyear = datecyear.split("-")
		datecday = int(datecyear[0])
		datecmonth = int(datecyear[1])
		datecyear = int(datecyear[2])
		print "printing..."
		
		datelyear = d.date.split("-")
		datelday = int(datelyear[0])
		datelmonth = int(datelyear[1])
		datelyear = int(datelyear[2])
		
		

		if((datecyear == datelyear) and (datecmonth == datelmonth) and (datecday == datelday)) :
			print "datematch"	


			shh = d.start_time.split(":")
			curtime_list = []
			
			
			
			smm = int(shh[1])
			shh = int(shh[0])
			

			ehh = d.end_time.split(":")
			
			emm = int(ehh[1])
			ehh = int(ehh[0])
			
			

			chh=shh
			cmm=smm			
				
				
			
			datecheck = str(datetime.date.today()+datetime.timedelta(days=2) )
			

			while(chh<ehh) :

				flag = 1 #for addind to timelist

				if(chh==12):
					ctime=str(chh)+':'+str(cmm)+" "+'PM'

				elif( chh<12):
					ctime=str(chh)+':'+str(cmm)+" "+'AM'
				else :
					thh=(chh%12)
					ctime=str(thh)+':'+str(cmm)+" "+'PM'
				
				# searching in bookdetails
				searchtable =  BookDetails.objects.filter(doc_name = data['docusername'])
				for s in searchtable :
					if s.date == datecheck:
						if s.doc_name == doc.doc_username :
							for n in loc : 
								if n.location == s.location :
									if s.time_slot == ctime :
										flag = 0
					 
					 
					 

								
				if flag == 1 :
					curtime_list.append(ctime)
				cmm += d.duration
				if(cmm >= 60):
					if(chh < 23) :
						chh+=1	
						cmm=cmm%60
					else :
						break
				
				
				
				
				
			



			daythreetime_list.append(curtime_list)

		
	
	context = {
		"doctor" : doc,
		"locs" : loc,
		"bookdet" : localist,
		"dayonetime" : dayonetime_list,
		"daytwotime" : daytwotime_list,
		"daythreetime" : daythreetime_list,
		"dates" : date_list


	}




	return render(request,'docprofile.html',context)

def bookDoc(request) :
	data = request.GET
	print data['timeslot']
	print data['booklocation']
	print data['bookdate']
	doc = Locations.objects.get(location =  data['booklocation'] )
	bookid = str(doc.doc_id) + data['booklocation'] + data['bookdate'] + data['timeslot']
	print doc.doc_id
	print bookid
	# bookdet.doc_name = doc.doc_id
	# bookdet.location = data['booklocation']
	# bookdet.time_slot = data['timeslot']
	# bookdet.save()
	
	context = {
		"time" : data['timeslot'],
		"location" : data['booklocation'],
		"date" : data['bookdate'],
		"doctor" : doc.doc_id
		


	}

	return render(request,'confirmationpage.html',context)
def confirm(request) :
	data = request.GET
	bookdet = BookDetails()

	bookdet.doc_name = data['dname']
	bookdet.location = data['location']
	bookdet.time_slot = data['timeslot']
	bookdet.patientname = data['Pname']
	bookdet.patientphone = data['Phone']
	bookdet.date = data['date']
	

	bookdet.save()
	context = {
		"bookid" : bookdet.id
	}
	return render(request,'booked.html',context)
def locdetail(request) :
	data = request.GET
	print data
	print data['date']
	print data['location']
	print data['starttime']	 
	loc = Locations.objects.get(location =  data['location'] )
	bookdoc = BookDoc()
	bookdoc.loc_id = loc
	bookdoc.date = data['date']
	bookdoc.start_time = data['starttime']	
	bookdoc.end_time = data['endtime']	
	bookdoc.duration = data['duration']
	bookdoc.save()



	return render(request,"index.html")


