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
    

    print("Hello %s\nYour decrypted message is: %s" % a[0], Decode())
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





def Decode(str):
    decoded= ''
    i = 0
    while(i < query.length):
        codeChar = query[i]
        codeNum = ord(codeChar)
        codeNum -= 3
        
        if(codeNum < 32  ||  126 < newCharCode){
            #underflow exception
            if(codeNum < 32){
                underBy = 32 - codeNum;
                newCodeNum = 127 - underBy;
            }
            #overflow exception
            if(126 < codeNum){
                overBy = codeNum - 126;
                newcodeNum = 31 + overBy;
            }
        }
            
        
        decodedChar = chr(newCodeNum)
        decoded[i] = decodedChar
        i += 1
    return decoded
