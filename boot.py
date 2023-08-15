import network
import esp
import machine 
 
esp.osdebug(None)       
esp.osdebug(0)
From ="aursun.py"
to = "main.py"

def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())

#print("Booting.. start")

setup=0

# check the state of file
file=open(From,"r")
get=file.read()
if  len(get):
    setup=1;
file.close()

#print(" status:"+str(setup))
# if aursun exit any content then copy it
if setup==1:
 #print("New setup!")   
 with open(to,"w") as into:
   get=open(From,"r")
   into.write(get.read())
   get.close()
   into.close()

# check whether file is having content

if setup==1:
   # print("Now old one is cleaning !")
    with open(From,"w") as file:
        file.write("")
        file.close()
        machine.soft_reset()
