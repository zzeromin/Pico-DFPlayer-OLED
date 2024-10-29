#picozero: https://picozero.readthedocs.io/en/latest/index.html

from picozero import LED
from time import sleep

led = LED(22)

#led.on()
#sleep(1)
#led.off()


#while True:
#    led.toggle()
#    sleep(1)

#led.blink()

led.pulse()

