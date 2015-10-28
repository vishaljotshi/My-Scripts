
#   Specify requirements here
###########
#partial prop files
data=["locationdevicemapping","jdbc","content","cms-content","tvguide","amqp","speeddialno","schedule","content","raulandborg","mappingservice","ordering","rtls","directory","drugeducation","encryption","hl7Handler","pathwayService","patientservice","presence-application","screenshare","usertask","foodOrdering"]

#all prop files

#data=["amqp","cms-content","commonsparserutil","content","directory","drugeducation","encryption","foodOrdering","hl7Handler","jdbc","locationdevicemapping","mappingservice","ordering","pathwayService","patientservice","presence-application","presence-cache","presence-rabbitmq","raulandborg","rtls","schedule","screenshare-hazelcast","screenshare","speeddialno","tvguide","usertask","version"]
outFile=open("query.sql",'w')


def dump(fileName,service,module):
    global outFile
    
    outFile.write("--\n-- "+service+"-- \n\n")
    outFileBuffer=""
    path="C:/opt/cisco/iep/mes/conf/"

    propFile=path+fileName
    fdata=open(propFile,'r').read()
    line=fdata.split('\n')

    linenum=0

    for l in line:
        linenum += 1
        #print linenum
        if(l.strip()!=''):
                if(l[0]!='#'):
                        l=l.strip()
                        x = l.split('=')
                        length=len(x)
                        if(length==2):
                            outFileBuffer += "insert into config_registry(service,module,configKey,configValue) values('"+service+"','"+module+"','"+x[0].strip()+"','"+x[1].strip()+"');"+"\n"
                        else:
                            i=2
                            while(i!=len(x)):
                                x[1] += '=' + x[i].strip()
                                i += 1
                            outFileBuffer += "insert into config_registry(service,module,configKey,configValue) values('"+service+"','"+module+"','"+x[0].strip()+"','"+x[1].strip()+"');"+"\n"
                            i=2
    outFile.write(outFileBuffer)    
#main function

for name in data:
    dump(name+'.properties',name,"MES")
    print name+" done !!"
    
