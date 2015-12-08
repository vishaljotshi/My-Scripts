import psutil,time,colorama
from colorama import Fore, Back
safeList={}
newList={}

colorama.init()
for process in psutil.process_iter():
    safeList[process.pid]=process.name()

while(True):
    time.sleep(0.5)
    for process in psutil.process_iter():
        if(process.pid not in safeList):
            try:
                #process.terminate()
                print Fore.GREEN+"[+] New Process : "+ process.name()+" "+str(process.pid)+Fore.WHITE
                safeList[process.pid]=process.name()
            except:
                print "---exception occured----"

    for pid,name in safeList.items():
        try:
            proc=psutil.Process(pid)
        except:
            print Back.RED+"[-] Terminated  : " + name + " "+str(pid)+Back.BLACK
            del safeList[pid]
            
                
