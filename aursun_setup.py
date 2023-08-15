import machine
import network
import socket
import time
import esp
from machine import Timer
from machine import Pin
import os
p2313123131231=Pin(2,Pin.OUT)
esp.osdebug(None)
esp.osdebug(0)
store123131123113 ="aursun.py"
ap1231213131=network.WLAN(network.AP_IF)
ap1231213131.config(essid="SoniBlocks") 
ap1231213131.config(max_clients=5)
ap1231213131.active(True)
sock2131311131 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2131311131.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
sock2131311131.bind(("192.168.4.1",21))
sock2131311131.setblocking(False) 
sock2131311131.listen(5)
bootMode12345646511="#2"
data123456789797877=""
state1234567891=0
def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())

def runcode____________________1234565(info):
 global data123456789797877
 global state1234567891
 state1234567891=""  
 if ap1231213131.isconnected():
      try:
           connection123131 = sock2131311131.accept()[0]           
           start21313113=0 
           while True:                        
            get=connection123131.recv(1).decode("utf8")          
            if start21313113==1:
                data123456789797877+=get 
            if get=='`':
              p2313123131231.on() 
              start21313113=1
            elif get=='~':
               p2313123131231.off()
               data123456789797877=data123456789797877[:-1]
               print("Set:"+data123456789797877)
               if data123456789797877[0:2]==bootMode12345646511:
                 state1234567891=bootMode12345646511
                 data123456789797877=data123456789797877[3:-1]     
                 if state1234567891==bootMode12345646511:
                  try:
                   with open(store123131123113,"w") as file:
                    file.write(data123456789797877)
                    file.close()
                  finally:
                      data123456789797877=""
                      run("boot.py")
                                     
               start21313113=0
               get=""
            else:
                print(get)
      except OSError as f:           
              pass