import urllib, urllib2, cookielib,re
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
resp=opener.open('http://lunch.gslab.com').read()
token=re.findall('name="authenticity_token" type="hidden" value="(.*?)" />',resp)

login_data = urllib.urlencode({'authenticity_token' : token, 'emp_id' : 'GS-1010', 'password' : 'metasploit!7728'})
login_resp=opener.open('http://lunch.gslab.com/login',login_data).read()

snacks_menu=re.findall("<font color='#12B2E2' style='font-size:14px;'>\n(.*)",login_resp)[0]

lunch_menu=re.findall("<font color='#12B2E2'>\n(.*)\n.*\n(.*)\n.*\n(.*)\n.*\n(.*)\n.*\n(.*)\n.*\n(.*)\n.*\n(.*)\n.*\n(.*)",login_resp)