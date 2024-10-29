"""
#Reference:
picozero: https://picozero.readthedocs.io/en/latest/index.html
picodfplayer: https://github.com/mannbro/PicoDFPlayer
SSD1306: https://micropython-docs.readthedocs.io/en/latest/esp8266/tutorial/ssd1306.html
"""
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep
from picozero import Button, LED
from picodfplayer import DFPlayer

# Button & LED pins
led = LED(22)
btn1 = Button(6) # play next song
btn2 = Button(7) # play current song
btn3 = Button(8) # pause

# Song data
song_names = [
    "My own jukebox",
    "Height measuring",
    "College experience",
    # Add more songs as needed
]
total_songs = len(song_names)
current_song_index = 0
volume = 15 # Initial volume level (0-30)

# Initialize OLED display
i2c = I2C(1, sda=Pin(2), scl=Pin(3), freq=400000)
display = SSD1306_I2C(128, 64, i2c)

#Constants. Change these if DFPlayer is connected to other pins.
UART_INSTANCE = 0
TX_PIN = 12
RX_PIN = 13
BUSY_PIN = 14

#Create player instance
player = DFPlayer(UART_INSTANCE, TX_PIN, RX_PIN, BUSY_PIN)
player.setVolume(15)

def play_song(song_index):
    if player.queryBusy() == False:
        # Replace this with your DFPlayer play command using the song index + 1
        # (DFPlayer uses 1-based indexing)
        print(f"Playing song: {song_names[song_index]} (index: {song_index + 1})")
        player.playTrack(1,song_index+1)
        display.fill(0)
        display.text("Now Playing:", 0, 0)
        display.text(song_names[current_song_index], 0, 20)
        display.text(f"Volume: {volume}", 0, 50)
        display.show()
        pass

def next_show(song_index):
    print(f"next ==> {song_names[current_song_index]} (index: {current_song_index + 1})")
    display.fill(0)
    display.text("Next Song:", 0, 0)
    display.text(song_names[song_index], 0, 20)
    display.text(f"Volume: {volume}", 0, 50)
    display.show()
    sleep(1)
    play_song(current_song_index)
    pass

def pause_show(song_index):
    player.pause()
    print(f"Player Paused!")
    display.fill(0)
    display.text("Player Paused!", 0, 0)
    display.text(song_names[song_index], 0, 20)
    display.text(f"Volume: {volume}", 0, 50)
    display.show()
    pass

def init_oled():
    display.fill(0)
    display.text("Select Song:", 0, 0)

    # Display song list
    for i in range(total_songs):
        if i == current_song_index:
            display.text(song_names[i], 0, 10 + i * 10)  # Highlight current song
        else:
            display.text(song_names[i], 0, 10 + i * 10)
    display.text(f"Volume: {volume}", 0, 50)
    display.show()    
    
led.on()
init_oled()
current_song_index = 0

while True:   
    
    if btn2.is_pressed:
        play_song(current_song_index)        
        sleep(0.2)
        
    if btn1.is_pressed:
        current_song_index = (current_song_index + 1) % total_songs        
        next_show(current_song_index)
        sleep(0.2)
        
    if btn3.is_pressed:
        if player.queryBusy() == False:
            pause_show(current_song_index)
            
    #if btn3.is_pressed:
    #    current_song_index = (current_song_index - 1 + total_songs) % total_songs
    #    print(f"prev ==> {song_names[current_song_index]} (index: {current_song_index + 1})")
        sleep(0.2)
        
    #btn1.when_pressed = track1
    #btn2.when_pressed = track2
    #btn3.when_pressed = track3