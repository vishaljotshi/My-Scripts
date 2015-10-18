from socket import *
import os
s=socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",800))
s.listen(5)
while True:
    c,a=s.accept()
    print "Received connecion from ", a
    req=c.recv(2048)
    fname=req.split("\r\n")[0].split(" ")[1]
    if fname=="/":
        fname="/index.html"
    fileptr = open("/sdcard/www" + fname,'r')
    code = fileptr.read()
    buf=("HTTP/1.1 200 OK\n"
    "Server: Fake Python Server/2.2.22\n"
    "Keep-Alive: timeout=5, max=100\n"
    "Date: Sun, 15 Sep 2013 20:39:26 GMT\n"
    "Content-Type: text/html;charset=UTF-8\n"
    "Content-length: " + str(len(code)) +
    "\nConnection: Keep-Alive\n\n" + code)
    c.send(buf)
