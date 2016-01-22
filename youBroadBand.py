import urllib, urllib2, cookielib,re
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'login' : 'joshi_998', 'password' : '197229', 'select' : 'https://itapps.youbroadband.in/default/homeuser/login_sql.jsp','appsname':''})
#login_data='login=joshi_998&password=197229&select=https%3A%2F%2Fitapps.youbroadband.in%2Fdefault%2Fhomeuser%2Flogin_sql.jsp&appsname='
login_success=opener.open('https://itapps.youbroadband.in/default/homeuser/login_sql.jsp', login_data)
resp = opener.open('https://itapps.youbroadband.in/default/susage/mybalance.jsp')
data= resp.read()
dataLeft=re.findall('<td align="center" valign="middle" bgcolor="#FFFFFF" width="130" class="breadcrum-link">(.*?)</td>',data)
print "Total data left : " + str(int(float(dataLeft[0]))/1024) +' GB'
print "Days left : "+dataLeft[1]