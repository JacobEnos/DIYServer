#CGI connection
#from BaseHTTPServer import HTTPServer
#from CGIHTTPServer import CGIHTTPRequestHandler
import os
#os.chdir("/home/docs/html")
#serv = HTTPServer(("",8080),CGIHTTPRequestHandler)
#serv.serve_forever()

#TCP connection
from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.bind(("localhost",65534))
s.listen(5)
while True:
    c,a = s.accept()
    print ("Received connection from", a)
    
    
    query = ''
    if os.environ['REQUEST_METHOD'] == 'GET':
        query = os.environ['QUERY_STRING']

    if os.environ['REQUEST_METHOD'] == 'POST':
        size = int(os.environ['CONTENT_LENGTH'])
        query = sys.stdin.read(size)
    

    c.send("Hello %s\nYour reversed message is: %s" % a[0], Reverse())
    c.close()



#Data reassembly
fragments = [] # List of chunks
while not done:
    chunk = s.recv(maxsize) # Get a chunk
    if not chunk:
        break # EOF. No more data
    fragments.append(chunk)
# Reassemble the message
message = "".join(fragments)





def Reverse(str):
    reversed= ''
    i = query.length -1
    j = 0
    while(i >=0):
        reversed[j] = query[i]
        j = j+1
        i = i-1
    return reversed



getElementById('Response').innerHTML = "Reversed: " + reversed
