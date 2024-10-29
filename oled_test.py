#SSD1306: https://micropython-docs.readthedocs.io/en/latest/esp8266/tutorial/ssd1306.html

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep

i2c = I2C(1, sda=Pin(2), scl=Pin(3), freq=400000)
display = SSD1306_I2C(128, 64, i2c)

print("I2C : " + str(i2c))

display.fill(0)
display.show()

display.text("Hello World", 10, 10)
display.show()
sleep(2)

