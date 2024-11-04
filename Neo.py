from machine import Pin
from neopixel import Neopixel
 
# Brugbare konstanter
white = (255, 255, 255)
red = (255, 0, 0)
orange = (255, 127, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
mint = (0, 255, 255)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (148, 0, 211)
black = (0, 0, 0)

pixPin = 0 # GPIO pin 0
pixNum = 8
pix = Neopixel(pixNum, 0, Pin(pixPin), "RGB")
 
pix.fill(black)
pix[0] = blue
pix.show()
