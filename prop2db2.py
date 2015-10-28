
#   Specify requirements here
###########
#partial prop files
data=['']
outFile=open("query.sql",'w')


def dump(fileName,service,module):
    global outFile
    
    outFile.write("--\n-- "+service+"-- \n\n")
    outFileBuffer=""
    path="C:/opt/*****/iep/mes/conf/"

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
    dump(name+'.properties',name,"***")
    print name+" done !!"
    
