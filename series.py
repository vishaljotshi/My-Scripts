import re,gzip,urllib2
from StringIO import StringIO
from bs4 import BeautifulSoup
from sets import Set

class Serial:
    name=''
    latestEpisode=''



srcZip=urllib2.urlopen("https://kat.cr/tv/").read()
stringBuffer=StringIO(srcZip)
plainSource=gzip.GzipFile(fileobj=stringBuffer).read()

s=Set()

soup=BeautifulSoup(plainSource,'html.parser')
a=soup.find_all("a",class_="cellMainLink")
for e in a:
    for x in re.findall('(.*?)\s(S\d{1,2}E\d{1,2})',e.get_text()):
        s.add(x[0])
for obj in list(s):
    print obj
