import psutil,time
safeList=[]
newList=[]

for process in psutil.process_iter():
    safeList.append(process.pid)

while(True):
    time.sleep(0.5)
    for process in psutil.process_iter():
        if(process.pid not in safeList):
            try:
                #process.terminate()
                print "New Process :"+ process.name()+" "+str(process.pid)
                safeList.append(process.pid)
                #try:
                #    print process.open_files()
                #except:
                #   pass
            except:
                print "---exception occured----"

    for pid in safeList:
        try:
            proc=psutil.Process(pid)
        except:
            print "Terminated :" + str(pid)
            try:
                safeList.remove(pid)
            except:
                pass
                
