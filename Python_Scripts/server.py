from http.server import BaseHTTPRequestHandler, HTTPServer

import os
from HOST_DATA_READ import Ae
#change this to the file location in your computer 
myrequestsk = None
myrequestemp = None
mystatus = None
class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global myrequestsk


    g=Ae()
    print('you got this requests')
    myrequestsk = self.requestline
    print('cleaned request')
    myrequestsk = myrequestsk[5 : int(len(myrequestsk) - 9)]
    print(myrequestsk)
    messagetosend=bytes(g,"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    return


server_address_httpd = ('192.168.137.21',8080)
#change this to your pc ip adress (cmd windows -ifconfig,terminal ubuntu -ipconfig)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('starting the server ')
httpd.serve_forever()

