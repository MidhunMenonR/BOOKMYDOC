import urllib2
import cookielib

def sendMessage(message,number):
	username = '7293257583'
	passwd = 'G2856G'
	message = 'Message from BookMyDoc:  %s.'%message
	#Logging into the SMS Site
	url = 'http://site24.way2sms.com/Login1.action?'
	data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
	 
	#For Cookies:
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	 
	# Adding Header detail:
	opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
	 
	try:
	    usock = opener.open(url, data)
	except IOError:
		return False
		pass
	     
	jession_id = str(cj).split('~')[1].split(' ')[0]
	send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
	send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
	opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
	 
	try:
	    sms_sent_page = opener.open(send_sms_url,send_sms_data)
	    return True
	except IOError:
		return False
		pass
	    

	    
