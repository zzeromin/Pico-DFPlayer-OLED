#In order ror this example-code to work, make sure you have a
#card with at least one folder, containing at least two mp3:s.
#The folders should be named 01, 02 etc and files should be named
#001.mp3, 002.mp3 etc.
from time import sleep
from picozero import Button, LED
from picodfplayer import DFPlayer

led = LED(22)
btn1 = Button(6)
btn2 = Button(7)
btn3 = Button(8)

#Constants. Change these if DFPlayer is connected to other pins.
UART_INSTANCE = 0
TX_PIN = 12
RX_PIN = 13
BUSY_PIN = 14

#Create player instance
player = DFPlayer(UART_INSTANCE, TX_PIN, RX_PIN, BUSY_PIN)
player.setVolume(15)
led.on()

def track1():
#    if player.queryBusy() == False:
        print("button = 1")
        player.playTrack(1,1)
        
def track2():
#    if player.queryBusy() == False:
        print("button = 2")
        player.playTrack(1,2)
        
def track3():
#    if player.queryBusy() == False:
        print("button = 3")
        player.playTrack(1,3)
        
while True:
    btn1.when_pressed = track1
    btn2.when_pressed = track2
    btn3.when_pressed = track3