from machine import Pin
import time

LED1 = Pin(2,Pin.OUT)
LED2 = Pin(16,Pin.OUT)
BUT = Pin(0,Pin.IN)

while True:
    but_status = BUT.value()
    if(but_status == False):
        LED1.value(0)
        time.sleep(0.1)
        LED2.value(0)
        time.sleep(0.1)
        LED1.value(1)
        LED2.value(1)
        time.sleep(0.1)
    else:
        LED1.value(1)
        LED2.value(1)
        