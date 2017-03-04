from django.shortcuts import render
from django.conf import settings
from .models import DocDetails
from .models import Locations
from .models import BookDoc
from .models import BookDetails
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
					print "working"
					docobjectlist.append(d)
		else :
			docobjectlist = doctor
	elif data['srchname'] :
		docobjectlist = DocDetails.objects.filter(doc_name__icontains = data['srchname'])
									
						






			


	# if data['srchloc'] :
	# 	tloclist = []
	# 	slocations = Locations.objects.filter(area__icontains  = data['srchloc'])
	# 	for sl in slocations:
	# 		moredoctors = DocDetails.objects.get(doc_username = sl.doc_id)
	# 		if data['srchname'] :
	# 				tempdocobjectlist = []
	# 				sdoctors = DocDetails.objects.filter(doc_name__icontains = data['srchname'])
	# 				for sdo in sdoctors :
	# 					if sdo.doc_username == moredoctors.doc_username :
	# 						tempdocobjectlist.append(moredoctors)
	# 				if data['srchdept'] :
	# 					sdepts = DocDetails.objects.filter(doc_department__icontains  = data['srchdept'])
	# 					for sd in sdepts:
	# 						for temp in tempdocobjectlist :
	# 							if sd.doc_username == temp.doc_username :
	# 								docobjectlist.append(moredoctors)
	# 				else :
	# 					docobjectlist.append(moredoctors)



	# 		else :	
	# 			docobjectlist.append(moredoctors)	

							




	# if data['srchname'] :
	# 	sdoctors = DocDetails.objects.filter(doc_name__icontains = data['srchname'])
	# if data['srchloc'] :
	# 	slocations = Locations.objects.filter(area__icontains  = data['srchloc'])
	# if data['srchdept'] :	
	# 	sdepts = DocDetails.objects.filter(doc_department__icontains  = data['srchdept'])
	# # if data['srchloc'] :
	# # 	for sl in slocations:
	# # 		moredoctors = DocDetails.objects.filter(doc_username = sl.doc_id)
	# # 		for md in moredoctors:
	# # 			docobjectlist.append(md)
	# if data['srchname'] :
	# 	for sdo in sdoctors:
	# 		docobjectlist.append(sdo)
	# if data['srchdept'] :	
	# 	for sd in sdepts:
	# 		docobjectlist.append(sd)
	

	# docobjectlist=list(set(docobjectlist)) #to remove duplicates


	for d in docobjectlist:
		print d.doc_name
		print d.doc_phone

	context = {
		"doctorslist" : docobjectlist

	}



	return render(request,'searchpage.html',context)


def docdetails(request):
	data = request.GET
	time_list=[]
	localist = []
	time_list = []
	i=0
	
	

	doc = DocDetails.objects.get(doc_username = data['docusername'])
	loc = Locations.objects.filter(doc_id = doc.doc_username )


	print 'name' + doc.doc_name
	for l in loc :
		print 'location' + l.location
		print 'id' + str(l.id)
		# if i==0 :
		# 	locdet = BookDoc.objects.filter(loc_id = l.id)
		# 	i=1
		# else :
		# 	locdet += (BookDoc.objects.filter(loc_id = l.id))
		locdet = BookDoc.objects.filter(loc_id = l.id)
		localist += locdet


	for d in localist :
		print 'start_time' + d.start_time #.strftime('%I:%H %p')
		print 'address' + d.address
		print 'duration' + str(d.duration)
		shh = d.start_time.split(":")
		curtime_list = []
		
		
		print shh
		smm = int(shh[1])
		shh = int(shh[0])
		print smm
		print shh

		ehh = d.end_time.split(":")
		print ehh
		emm = int(ehh[1])
		ehh = int(ehh[0])
		
		print emm
		print ehh

		chh=shh
		cmm=smm

		while(chh<ehh) :

			flag = 1 #for addind to timelist
			if(chh==12):
				ctime=str(chh)+':'+str(cmm)+" "+'PM'

			elif( (chh%12)==0):
				ctime=str(chh)+':'+str(cmm)+" "+'AM'
			else :
				thh=chh%12
				ctime=str(thh)+':'+str(cmm)+" "+'PM'
			print ctime
			# searching in bookdetails
			searchtable =  BookDetails.objects.filter(doc_name = data['docusername'])
			for s in searchtable :
				for n in loc :
					if n.location == s.location :
						if s.time_slot == ctime :
							flag =0
							print 'notadded'

			if flag == 1 :
				curtime_list.append(ctime)
			cmm += d.duration
			if(cmm >= 60):
				if(chh < 23) :
					chh+=1	
					cmm=cmm%60
				else :
					break
			
			
			
			print curtime_list
			
		



		time_list.append(curtime_list)




		# print 'end_time' + d.end_time
		# time_list.append(d.start_time)
		# time_list.append(d.end_time)




	print time_list
	context = {
		"doctor" : doc,
		"locs" : loc,
		"bookdet" : localist,
		"times" : time_list

	}




	return render(request,'docprofile.html',context)

def bookDoc(request) :
	data = request.GET
	print data['timeslot']
	print data['booklocation']
	bookdet = BookDetails()
	doc = Locations.objects.get(location =  data['booklocation'] )
	print doc.doc_id
	bookdet.doc_name = doc.doc_id
	bookdet.location = data['booklocation']
	bookdet.time_slot = data['timeslot']
	bookdet.save()
	
	context = {
		"time" : data['timeslot']

	}

	return render(request,'confirmationpage.html',context)



