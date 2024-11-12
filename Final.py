from neopixel import Neopixel
from machine import Pin, ADC, PWM
import time
 
#Knap og potentiometer
button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
adc = ADC(Pin(26, mode=Pin.IN))
 
# Brugbare konstanter
fill = (0, 0, 0)
 
 
def map_to_rainbow_color(value):
    num_colors = 7  # Number of colors in the rainbow
    # Map the potentiometer value to the range of rainbow colors
    if value > 0 and value < 120:
        return (255, 0, 0)  # Red
    elif value > 121 and value < 240:
        return (255, 127, 0)  # Orange
    elif value > 241 and value < 360:
        return (255, 255, 0)  # Yellow
    elif value > 361 and value < 480:
        return (0, 255, 0)  # Green
    elif value > 481 and value < 600:
        return (0, 0, 255)  # Blue
    elif value > 601 and value < 720:
        return (75, 0, 130)  # Indigo
    elif value >721 and value < 840:
        return (148, 0, 211)  # Violet
    elif value >841 and value < 960:
        return (255, 255, 255)  # White
    elif value >961 and value < 3000:
        return (0, 0, 0)  # Black / off
   
 
pixPin = 0 # GPIO pin 0
pixNum = 8
pix = Neopixel(pixNum, 0, Pin(pixPin), "RGB")
#pix.fill(black)
#pix[0] = red
#pix.show()
 
 
while True:
    duty = adc.read_u16() #between ~350-65535
    low_res = duty >> 5
    neo_color = map_to_rainbow_color(int(low_res))
    pix.fill(fill)
    pix[0] = neo_color
    pix.show()
    time.sleep_ms(100)
    #print(low_res)
    #print('#%02x%02x%02x' % color)
    if not button.value():
        value = low_res
        color = '#%02x%02x%02x' % neo_color
        ID = "Sara"
        eye = "green"
       
        # Get current date and time in "YYYY-MM-DD HH:MM:SS" format
        timestamp = "{:04}-{:02}-{:02} {:02}:{:02}:{:02}".format(*time.localtime()[:6])
 
        # Append data to CSV file
        with open("mydata.csv", "a") as f:
            f.write(f"{value},{color},{timestamp},{ID},{eye}\n")
       
        print(value, color, timestamp, ID, eye)
        time.sleep_ms(200)
