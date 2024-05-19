from machine import Pin
from time import sleep

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    print(button.value())
    sleep(.5)
    if button.value() == 1:
        led.toggle()
        sleep(.5)
    else:
        led.value(0)
