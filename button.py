#picozero: https://picozero.readthedocs.io/en/latest/index.html

from picozero import LED, Button
from time import sleep

btn1 = Button(6)
led = LED(22)

while True:
    if btn1.is_pressed:
        print("Button is pressed")
        led.on()
    else:
        print("Button is not pressed")
        led.off()
    sleep(0.1)