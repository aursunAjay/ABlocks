from machine import UART
import bluetooth
import ble_uart_peripheral
import settings 
import _thread
import machine
import time

LED_PIN_1 = 2  # GPIO pin for LED 1
LED_PIN_2 = 4  # GPIO pin for LED 2

# Initialize the BLE stack
ble = bluetooth.BLE()

# Initialize the BLEUART peripheral
ble_uart = ble_uart_peripheral.BLEUART(ble)

data = ""

# Define a callback function to handle received data
activate_rec = 0

def on_uart_rx():
    global data
    global activate_rec
    check = ble_uart.read()   
    
    if check == '~':
         activate_rec = 1
   
    
    if activate_rec == 1:
        data+=check.decode("utf-8")
        check = ""
    
    ble_uart.write(check)
    
    if check == '#' and data != "":
        print(data)
        settings.file(data,"w")
        data = ""
        activate_rec = 0
        settings.run("main.py")
        
# Set the callback function
ble_uart.irq(on_uart_rx)

while True:
        try:
         while True:
          machine.Pin(LED_PIN_1, machine.Pin.OUT).value(1)  # Turn on LED 1
          time.sleep(1)  # Delay for 1 second
          machine.Pin(LED_PIN_1, machine.Pin.OUT).value(0)  # Turn off LED 1
          time.sleep(1)  # Delay for 1 second          
        except KeyboardInterrupt:
          pass
  
 
ble_uart.close()



