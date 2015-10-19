import re,gzip,urllib2
from StringIO import StringIO
from bs4 import BeautifulSoup
from sets import Set

objList=[]

class Serial:
    name=''
    season=1
    episode=1
    def __init__(self,name,season,episode):
        self.name=name
        self.season=season
        self.episode=episode

def list_add(serial):
    global objList
    flag=0
    for obj in objList:
        flag=0
        if(obj.name!=serial.name):
            #not present
            #objList.append(serial)
            flag=0
        else:
            flag=1
            if(int(obj.episode)<int(serial.episode)):
                objList.remove(obj)
                objlist.append(serial)
    if(flag==0):
        objList.append(serial)
        
    


s=Set()


srcZip=urllib2.urlopen("https://kat.cr/tv/").read()
stringBuffer=StringIO(srcZip)
plainSource=gzip.GzipFile(fileobj=stringBuffer).read()


soup=BeautifulSoup(plainSource,'html.parser')
a=soup.find_all("a",class_="cellMainLink")
for e in a:
    for x in re.findall('(.*?)\sS(\d{1,2})E(\d{1,2})',e.get_text()):
        serial=Serial(x[0],x[1],x[2])
        list_add(serial)

print len(objList)      
for obj in objList:
    print 'name : ' + obj.name + "   season : "+obj.season+" episode : "+obj.episode
    
