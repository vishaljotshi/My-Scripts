import psutil,time
safeList={}
newList={}

for process in psutil.process_iter():
    safeList[process.pid]=process.name()

while(True):
    time.sleep(0.5)
    for process in psutil.process_iter():
        if(process.pid not in safeList):
            try:
                #process.terminate()
                print "[+] New Process : "+ process.name()+" "+str(process.pid)
                safeList[process.pid]=process.name()
            except:
                print "---exception occured----"

    for pid,name in safeList.items():
        try:
            proc=psutil.Process(pid)
        except:
            print "[-] Terminated  : " + name + " "+str(pid)
            del safeList[pid]
            
                
