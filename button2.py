#picozero: https://picozero.readthedocs.io/en/latest/index.html

from picozero import Button, LED
from time import sleep

led = LED(22)
btn1 = Button(6)
btn2 = Button(7)
btn3 = Button(8)

while True:
    btn1.when_pressed = led.on
    btn2.when_pressed = led.off
    btn3.when_pressed = led.blink