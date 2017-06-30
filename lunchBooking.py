import urllib, urllib2, cookielib,re
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
resp=opener.open('http://lunch.gslab.com').read()
token=re.findall('name="authenticity_token" type="hidden" value="(.*?)" />',resp)[0]
print token

login_data = urllib.urlencode({'authenticity_token' : token, 'emp_id' : 'GS-1010', 'password' : '!h4ck3rmvjmvjMVJ'})
print "Token:"+token
login_resp=opener.open('http://lunch.gslab.com/login',login_data).read()

snacks_menu=re.findall("<font color='#12B2E2' style='font-size:14px;'>\n(.*)",login_resp)[0]

lunch_menu=re.findall("<font color='#12B2E2'>\n(.*)\n.*\n(.*)\n.*\n(.*)\n.*\n(.*)\n.*\n(.*)\n.*\n(.*)\n.*\n(.*)\n.*\n(.*)",login_resp)

print snacks_menu
print lunch_menu

print "Placing order for lunch and snacks"

lunch_order_data = urllib.urlencode({'authenticity_token' : token, 'emp_id' : 'GS-1010', 'password' : '!h4ck3rmvjmvjMVJ','first_name':'Vishal','last_name':'Jotshi','email':'vishal.jotshi@gslab.com','order_type':'lunch','location':'Amar Arma Gensis'})
booking_resp=opener.open('http://lunch.gslab.com/user/toggle_order',lunch_order_data).read()

print booking_resp


##
##order_type=lunch&empid=GS-1010&first_name=Vishal&last_name=Jotshi&email=vishal.jotshi%40gslab.com
##&location=Amar+Arma+Gensis&authenticity_token=ItnTq0sNEYta51dJXGXvUDYnMR5BDeZcpmhoDJrU8KA%3D
##POST http://lunch.gslab.com/user/toggle_order
##
##
##order_type=snacks&empid=GS-1010&first_name=Vishal&last_name=Jotshi&email=vishal.jotshi%40gslab.com&location=Amar+Arma+Gensis&authenticity_token=ItnTq0sNEYta51dJXGXvUDYnMR5BDeZcpmhoDJrU8KA%3D
##
##
##POST /user/toggle_order HTTP/1.1
##Host: lunch.gslab.com
##Connection: keep-alive
##Content-Length: 189
##Origin: http://lunch.gslab.com
##X-CSRF-Token: rtIg9LyDo63D7R3V42ewKXuAqLkROWYja30ZBT5p41A=
##User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36
##Content-Type: application/x-www-form-urlencoded; charset=UTF-8
##Accept: */*
##X-Requested-With: XMLHttpRequest
##Referer: http://lunch.gslab.com/user
##Accept-Encoding: gzip, deflate
##Accept-Language: en-US,en;q=0.8
##Cookie: _amhungry_session=BAh7CEkiCmVtcGlkBjoGRUZJIgxHUy0xMDEwBjsAVEkiD3Nlc3Npb25faWQGOwBGSSIlNzcxZWRiOTJjNTAxYzBmZTAxZDA1MmZhZGQ2ZjU5ZTYGOwBUSSIQX2NzcmZfdG9rZW4GOwBGSSIxcnRJZzlMeURvNjNEN1IzVjQyZXdLWHVBcUxrUk9XWWphMzBaQlQ1cDQxQT0GOwBG--47d9c51718c3bf69e4b8649f24c1dd1317cec95f
