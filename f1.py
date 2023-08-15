import _thread
import machine
import time

LED_PIN_1 = 2  # GPIO pin for LED 1
LED_PIN_2 = 4  # GPIO pin for LED 2

def thread1():
    while True:
        aursun_setup.runcode____________________1234565("ok")
        machine.Pin(LED_PIN_1, machine.Pin.OUT).value(1)  # Turn on LED 1
        time.sleep(1)  # Delay for 1 second
        machine.Pin(LED_PIN_1, machine.Pin.OUT).value(0)  # Turn off LED 1
        time.sleep(1)  # Delay for 1 second

def thread2():
    while True:
        machine.Pin(LED_PIN_2, machine.Pin.OUT).value(1)  # Turn on LED 2
        time.sleep(0.5)  # Delay for 500 milliseconds
        machine.Pin(LED_PIN_2, machine.Pin.OUT).value(0)  # Turn off LED 2
        time.sleep(0.5)  # Delay for 500 milliseconds

_thread.start_new_thread(thread1, ())
_thread.start_new_thread(thread2, ())
