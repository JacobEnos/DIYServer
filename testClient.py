import sys
from socket import *
from urllib import *
import urllib.parse
import urllib.request

msgIn = input("Message to be reversed: ")
data = urllib.parse.urlencode({ 'message' : msgIn })
data = data.encode("ascii")


s = socket(AF_INET,SOCK_STREAM)
serverAddress = ('cis-linux2.temple.edu', 8080)
s.connect(serverAddress) # Connect


headers = {
    'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 2.0.50727)',
    'Content-type' : 'text',
    'Content-length' : 1500
}

r = urllib.request.Request("http://cis-linux2.temple.edu:8080/SP20_3344_tug99053/NetworkArchitectures/Server.py", data, headers)
u = urllib.request.urlopen(r)
if u.code == 200:
    print("success")
elif u.code == 404:
    print("Not found!")
elif u.code == 403:
    print("Forbidden")


s.sendall(b"POST /SP20_3344_tug99053/NetworkArchitectures/Server.py HTTP/1.0\n\n") # Send request
data = s.recv(10000) # Get response


#display data
print(data)

s.close()

