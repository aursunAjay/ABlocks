
import machine
import network
import socket
import time
import esp
from machine import Timer
from machine import Pin
import os


print("settings")

__IP__ = "192.168.4.1"
__F1__ = 1				# constants for file sections
__F2__ = 0
__APPEND__ = "a"
__WRITE__ = "w"
__BOOT_MODE__  		 = "#2#"
__NEW_FIRMWARE__ 	 = 1   # Constants for firmware selection


__F1_NAME__ 	= "f1.py"
__F2_NAME__ 	= "main.py"
__TEMP_BUFFER__ = "temp_buffer.txt"

__WIFI_STATUS__      = 0   #standard wifi status flag              1 > signals 0 > no signals   

__FIRMWARE_MODE__    = 0   #Standard firmware toggle flag          1 > f1.py   0 > f2.py 

__FIRMWARE_STATUS__  = 0   # standard firmware update status flag  1 > new firmware  0 > no update


def run(runfile):
    with open(runfile, "r") as rnf:
        exec(rnf.read())
    
def encrypt(text, key):
    encrypted = ''
    for char in text:
        encrypted_char = chr(ord(char) ^ key)
        encrypted += encrypted_char
    return encrypted

def decrypt(ciphertext, key):
    decrypted = ''
    for char in ciphertext:
        decrypted_char = chr(ord(char) ^ key)
        decrypted += decrypted_char
    return decrypted    

# Write data to a file
def file(data,flag):
 try:        
    with open(file_path,flag) as file:
        file.write(data)
        print("Data written to the file")
 except OSError:
        print("Error reading the file")
        
def read_from_file():
    try:
        with open(file_path, "r") as file:
            data = file.read()
            print("Data read from the file:", data)
            return data
    except OSError:
        print("Error reading the file")
               

p2313123131231=Pin(2,Pin.OUT)
__CONNECTION__=network.WLAN(network.AP_IF)
__CONNECTION__.config(essid="SoniBlocks") 
__CONNECTION__.config(max_clients=5)
__CONNECTION__.active(True)
__SOCKET__ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
__SOCKET__.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
__SOCKET__.bind(__IP__,21))
__SOCKET__.setblocking(False) 
__SOCKET__.listen(5)