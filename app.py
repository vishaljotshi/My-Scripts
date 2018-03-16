import hmac,requests
from bs4 import BeautifulSoup

##pips : bs4,lxml
headers={"X-ClientVersion":"3.7.1","X-Unity-Version":"5.5.3p4","X-OS":"Android OS 4.4.4 / API-19 (KTU84P/eng..20171228.113339)","Content-Type":"application/xml","Cache-Control":"no-cache","User-Agent":"Dalvik/1.6.0 (Linux; U; Android 4.4.4; SM-G950F Build/KTU84P)","Host":"gpwarrobots.pixapi.net","Connection":"close","Accept-Encoding":"gzip, deflate"}    

def dgst(message):
    h=hmac.new('TawejLetlemvijRuaskunCobMetlyinlapBagCyojtabixhyilvarUlorcyo',message);
    return h.hexdigest()



def serverpost(api,data):
    headers["X-SIGNATURE"]=dgst(data)
    print "Digest :"+ dgst(data)
    r=requests.post(api,data, headers=headers)
    return r

def consumeResearch(rid):
    consumeApi="https://gpwarrobots.pixapi.net/api/lab/absorb"
    body="""<?xml version="1.0" encoding="utf-8"?>
    <beanWithLong>
    <value>"""+str(rid)+"""</value>
    </beanWithLong>"""

    response=serverpost(consumeApi,body)
    #print "Response length :" + str(len(response.text))
    rsp_bs=BeautifulSoup(response.text,'xml')
    print "After consuming Workshop Points = "+rsp_bs.rp.string

def startResearch():
    research_data="""<?xml version="1.0" encoding="utf-8"?>
    <beanWithInt>
    <analyticBundle>
    <source>laboratory_screen</source>
    </analyticBundle>
    <value>40000</value>
    </beanWithInt>"""

    api="https://gpwarrobots.pixapi.net/api/lab/addsimple"

    rsp=serverpost(api,research_data)
    print "Response length :" + str(len(rsp.text))
    


data="""<?xml version="1.0" encoding="utf-8"?>
<loginMessage>
  <identityType>Googleplay</identityType>
  <identityId>g18435845742057594959</identityId>
  <playerId>03f8475f-14ce-4e48-81be-ca04ab98b710</playerId>
  <locale>en</locale>
  <store>GOOGLE</store>
  <dateTime>2018-02-01T01:33:34.7877110+08:00</dateTime>
  <clientTime>1517420015</clientTime>
  <authCode>EXyGgos7JE2kegq2k82kuEUQPJJWJAsz+w2HYa0O3BswveWIQW/3+x4FWHaRtl5TqqoOsUdtQy3FLa64Y/XF2gxzrGdAUUgEUeKut4AfppO8F8l8CHXu3hNKcs6cKk6OKKKQaczpkj7U2r0y8djqSl2MI+WHLBjEAY7wXTLqZJg=</authCode>
</loginMessage>"""

resp=serverpost("https://gpwarrobots.pixapi.net/api/login/byidentity",data)

xmlresp=BeautifulSoup(resp.text,'xml')

#got token
token=xmlresp.sessionMessage.sessionId.get_text()
print "Token : "+token


#setting session header
headers["X-RestSession"]=token

print headers["X-RestSession"]


#Regular chest status
chestData="""<?xml version="1.0" encoding="utf-8"?>
<anyType />"""
resp=serverpost("https://gpwarrobots.pixapi.net/api/chest/regular/status",chestData)
#print resp.text

data="""
<?xml version="1.0" encoding="utf-8"?>
<anyType />
"""
resp=serverpost("https://gpwarrobots.pixapi.net/api/chest/regular/open",data)
#print resp.text



##### Open workshop points
data="""<?xml version="1.0" encoding="utf-8"?>
<anyType />"""

wspResponse=serverpost("https://gpwarrobots.pixapi.net/api/lab/get",data)
wspSoup=BeautifulSoup(wspResponse.text,'xml')
researches=wspSoup.find_all('researches')
print "Before consuming Workshop Points : "+wspSoup.rp.string

doneCount=0

for research in researches:
    researchBs=BeautifulSoup(str(research),'xml')
    print researchBs.id.string + " : " +researchBs.done.string
    if(researchBs.done.string=="true"):
        rid=researchBs.id.string
        doneCount +=1
        print "Consuming id "+rid
        consumeResearch(rid)

#start research

#doneCount=3

print "count="+str(doneCount)
while(doneCount!=0):
    startResearch()
    doneCount -= 1





    


