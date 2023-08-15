## Standard ESP32 file names as per written :-

1. boot.py
2. f1.py
3. main.py
4. settings.py


## Micropython Firmware installion steps -

Steps as per written below :- 

1. Install python 3 on your desktop machine   

2. Download esptool.zip file at your pc

3. Copy esptool folder path and add on your command prompt 
Example:   
   Path: C:\Users\AJASONI\Desktop\esptool       
   After added will look like as per below: 
   C:\Users\AJASONI\Desktop\esptool>

4. Check the Port so go to Device manager and check COM port like COM2 or COM3 etc if device is connected will show.

5. Erase the flash: python esptool.py --port COM7 erase_flash
Example:
C:\Users\AJASONI\Desktop\esptool> python esptool.py --port COM7 erase_flash

5. Upload the firmware : esptool --port COM7 --baud 115200 write_flash --flash_size=detect 0 file.bin
Example:-
C:\Users\AJASONI\Desktop\esptool>esptool --port COM7 --baud 115200 write_flash --flash_size=detect 0 file.bin

6. Now device is ready !

## Development status :- 
 - Async TCP server establishment inside boot.py file 
 - Async TCP server working testing
 - Async TCP server working after running second file
 - Multithreading implementation  
