from django.shortcuts import render
from django.conf import settings
from .models import DocDetails
from .models import Locations
from .models import BookDoc
from .models import BookDetails
from .models import EmergDoctor
import datetime
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pyfcm import FCMNotification
from fcm_django.models import FCMDevice
from sendSMS import sendMessage
# Create your views here.
# EmployeeDetails.objects.filter(...).delete()


def home(request):
	
	return render(request,'index.html')
#for location
global startExe
global applocation
global view
view = 0
startExe = False
applocation = ''
@csrf_exempt
def location(request):
	global startExe,applocation
	startExe = False
	data = request.body
	values = data.split("\"")
	print values[11]
	startExe = True
	applocation = values[11]
	str = "hello"
	print 'location called!: '+applocation
	context={"key": str}
	return JsonResponse(context)

@csrf_exempt
def sebin(request):
	date =request.body
	print data
	str = "hello"
	context={"key": str}
	return JsonResponse(context)

def about(request) :
	return render(request,'about.html')	

def apphome(request):
	global startExe,applocation
	while not startExe:
		continue
	print 'Value of startExe: '+str(startExe)

	print 'App loc : '+applocation
	context ={
		"location" : applocation
	}
	
	return render(request,'indexapp.html',context)
@csrf_exempt
def responsedoc(request):
	print "working"
	data = request.body
	print data
	response = data.split("\"")

	print response

	response = response[3]

	print response
	global view
	if response == 'Accept' :
		view = 1
	else :
		view = 2
	samplestr = "hello"
	context={"key": samplestr}
	return JsonResponse(context)
			
	

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

	bookings = BookDetails.objects.filter(doc_name = data['usrnm'] )
	context ={
		"title" : "Doctor",
		"model" : usr,
		"locations" : locs,
		"locationdetails" : locdets,
		"bookings" : bookings
	}
	if usr.doc_password == data['pwd'] :
		value = 1
		
		
		
	if value == 1:
		return render(request,'Doc-edit.html',context)

	else :	
		return render(request,'login.html',{})

def searchform(request):
	data = request.GET
	
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

def searchformapp(request):
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



	return render(request,'searchpageapp.html',context)


def docdetails(request):
	data = request.GET
	localist = []
	date_list = []
	dayonetime_list = []
	daytwotime_list = []
	daythreetime_list = []
	timesdict = {"loc1day1" : [],"loc1day2" : [],"loc1day3" : [],"loc2day1" : [],"loc2day2" : [],"loc2day3" : [],"loc3day1" : [],"loc3day2" : [],"loc3day3" : [] }



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
	
	lenghtloc = range(len(loc)) 

	for d in localist :
		for i in lenghtloc :
			if d.loc_id == loc[i] :
				print d.loc_id
				print loc[i]
				datecyear = str(date_list[0])
				datecyear = datecyear.split("-")
				datecday = int(datecyear[0])
				datecmonth = int(datecyear[1])
				datecyear = int(datecyear[2])
				
				datelyear = d.date.split("-")
				datelday = int(datelyear[0])
				datelmonth = int(datelyear[1])
				datelyear = int(datelyear[2])
				dayonetime_list = []
				daytwotime_list = []
				daythreetime_list = []

				if((datecyear == datelyear) and (datecmonth == datelmonth) and (datecday == datelday)) :
					
					shh = d.start_time.split(":")
					curtime_list = []
					
					smm = int(shh[1])
					shh = int(shh[0])
			

					ehh = d.end_time.split(":")
					
					emm = int(ehh[1])
					ehh = int(ehh[0])
					dayonetime_list = []
					daytwotime_list = []
					daythreetime_list = []
				
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
								
						if cmm<10 :
							strcmm = str(cmm) + '0'
						else :
							strcmm = str(cmm)

						if(chh==12):
							ctime=str(chh)+':'+strcmm+" "+'PM'

						elif( chh<12):
							ctime=str(chh)+':'+strcmm+" "+'AM'
						else :
							thh=(chh%12)
							ctime=str(thh)+':'+strcmm+" "+'PM'
						
						# searching in bookdetails
						if flag != 0 :
							searchtable =  BookDetails.objects.filter(doc_name = data['docusername'])
							
							for s in searchtable :
								if s.date == str(date_list[0]):

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
					dictk = 'loc'+ str(i+1)+ 'day1' 
					print dictk
					print dayonetime_list
					timesdict[dictk] = dayonetime_list[0]	
					

				#day2loc1		
				
				
				datecyear = str(date_list[1])
				datecyear = datecyear.split("-")
				datecday = int(datecyear[0])
				datecmonth = int(datecyear[1])
				datecyear = int(datecyear[2])
					
					
				datelyear = d.date.split("-")
				datelday = int(datelyear[0])
				datelmonth = int(datelyear[1])
				datelyear = int(datelyear[2])
				dayonetime_list = []
				daytwotime_list = []
				daythreetime_list = []
								
					

				if((datecyear == datelyear) and (datecmonth == datelmonth) and (datecday == datelday)) :
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
							if cmm<10 :
								strcmm = str(cmm) + '0'
							else :
								strcmm = str(cmm)

							if(chh==12):
								ctime=str(chh)+':'+strcmm+" "+'PM'

							elif( chh<12):
								ctime=str(chh)+':'+strcmm+" "+'AM'
							else :
								thh=(chh%12)
								ctime=str(thh)+':'+strcmm+" "+'PM'
							
							# searching in bookdetails
							searchtable =  BookDetails.objects.filter(doc_name = data['docusername'])
							for s in searchtable :
								if s.date == str(date_list[1]):
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
						dictk = 'loc'+ str(i+1)+ 'day2' 
						timesdict[dictk] = daytwotime_list[0]
						print daytwotime_list
			
				#day3loc1
				datecyear = str(date_list[2])
				datecyear = datecyear.split("-")
				datecday = int(datecyear[0])
				datecmonth = int(datecyear[1])
				datecyear = int(datecyear[2])
							
				datelyear = d.date.split("-")
				datelday = int(datelyear[0])
				datelmonth = int(datelyear[1])
				datelyear = int(datelyear[2])	
				dayonetime_list = []
				daytwotime_list = []
				daythreetime_list = []		
				
							
							

				if((datecyear == datelyear) and (datecmonth == datelmonth) and (datecday == datelday)) :
									
								

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

									if cmm<10 :
										strcmm = str(cmm) + '0'
									else :
										strcmm = str(cmm)


									if(chh==12):
										ctime=str(chh)+':'+strcmm+" "+'PM'

									elif( chh<12):
										ctime=str(chh)+':'+strcmm+" "+'AM'
									else :
										thh=(chh%12)
										ctime=str(thh)+':'+strcmm+" "+'PM'
									
									# searching in bookdetails
									searchtable =  BookDetails.objects.filter(doc_name = data['docusername'])
									for s in searchtable :
										if s.date == str(date_list[2]):
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
							dictk = 'loc'+ str(i+1)+ 'day3' 
							timesdict[dictk] = daythreetime_list[0]
		

	context = {
		"doctor" : doc,
		"locs" : loc,
		"bookdet" : localist,
		
		"dates" : date_list,
		"dict" : timesdict


	}
							
				

					


	




	return render(request,'docprofile.html',context)


	# return render(request,'docprofile.html',context)

def bookDoc(request) :
	data = request.GET
	
	doc = Locations.objects.get(location =  data['booklocation'] )
	bookid = str(doc.doc_id) + data['booklocation'] + data['bookdate'] + data['timeslot']
	
	
	
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


	#checking whether booking has already been done

	booked = 0

	docobj=BookDetails.objects.filter(doc_name = data['dname'] )
	for doc in docobj :
		if doc.location ==  data['location'] :
			if doc.date == data['date'] : 
				if doc.time_slot == data['timeslot'] :
					booked =1

	if booked == 0 :
		bookdet.save()
		phonenumber = str(data['Phone'])
		message = 'Booking Successfull\n Booking ID :' + str(bookdet.id) + '\nDoctor :'+ str(bookdet.doc_name) +'\nLocation :' + str(bookdet.location) +'\nDate: ' + str(bookdet.date) + '\nTime : ' + str(bookdet.time_slot) 
		sendMessage(message,phonenumber)
	

	
	
	context = {
		"book" : bookdet,
		"flag" : booked 
	}
	return render(request,'bookingid.html',context)
def locdetail(request) :
	data = request.GET	
	loc = Locations.objects.get(location =  data['location'] )
	bookdoc = BookDoc()
	bookdoc.loc_id = loc
	bookdoc.date = data['date']
	bookdoc.start_time = data['starttime']	
	bookdoc.end_time = data['endtime']	
	bookdoc.duration = data['duration']
	bookdoc.save()
	return render(request,"index.html")


def notification(request):
	data = request.GET
	push_service = FCMNotification(api_key="AAAA2QRgGlM:APA91bEQfIV13lQd8lF-QIS8EpPaj7k96NoclepMkS5XB37w9z9lP2iNXqWXw-h9NSlvdIVVe1ZFl9VDI9A3-cezk4DcI83Z2ZHjCQesqCGk7qZrzZGopOgWaEhA1VzRYn3WP7rG5Vbd")
	print "requesting for " + data['docusername']
	obj = EmergDoctor.objects.get(doctor = data['docusername'] )
	registration_id = obj.regtoken

	message_title = "Patient Request"
	message_body = "A patient requests your service "
	click_action = "com.example.midhun.fcmtest_NotifAct"

	result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body,click_action = click_action)

	global view
	while view == 0 :
		
		pass
	global views
	if view == 1 :
		view =0
		return render(request,"accept.html")
	if view == 2 :
		view =0
		return render(request,"reject.html")	

	
	return HttpResponse("Waiting for doctor's response.....")
def sample(request):
	return render(request,"ajaxtest.html")
@csrf_exempt
def ajaxlocationentry(request) :
	data = request.POST
	
	
	loc = Locations.objects.get(location =  data['location'] )
	bookdoc = BookDoc()
	bookdoc.loc_id = loc
	bookdoc.date = data['date']
	bookdoc.start_time = data['starttime']	
	bookdoc.end_time = data['endtime']	
	bookdoc.duration = data['duration']
	bookdoc.save()


	return HttpResponse(bookdoc.id)

@csrf_exempt
def ajaxlocationrem(request) :
	data = request.POST
	
	bk = BookDoc.objects.get(id = data['id'])
	bk.delete()
	return HttpResponse("done")

@csrf_exempt	
def regtoken(request) :
	data = request.body
	valid = 0
	print 'data Received'
	print data
	
	token = data.split("\"")
	print 'split'
	


	usrname = token[3]
	pswd = token[7]
	regt = token[11]


	print 'username' + usrname
	print 'password' + pswd
	print 'token ' + regt

	usr = DocDetails.objects.get(doc_username =  usrname)
	if usr.doc_password == pswd :
		valid = 1
	print 'valid' + str(valid)
	if valid == 1 :
		string = "Valid"
		newdoc = EmergDoctor()
		newdoc.doctor = usrname
		newdoc.regtoken = regt
		newdoc.save()

	else :
		string = "Invalid"


	
	context={"key": string}
	return JsonResponse(context)


	# value = 0
	
	# usr = DocDetails.objects.get(doc_username=  data['usrnm'])

	# bookings = BookDetails.objects.filter(doc_name = data['usrnm'] )
	# context ={
	# 	"title" : "Doctor",
	# 	"model" : usr,
	# 	"locations" : locs,
	# 	"locationdetails" : locdets,
	# 	"bookings" : bookings
	# }
	# if usr.doc_password == data['pwd'] :
	# 	value = 1
		
		
		
	# if value == 1:
	# 	return render(request,'Doc-edit.html',context)

	# else :	
	# 	return render(request,'login.html',{})



	