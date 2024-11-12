#neopixel virker med potentiometer
from neopixel import Neopixel
from machine import Pin, ADC, PWM
import time

button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
pixels = Neopixel(5, 0, 0, "GRB") # no, state, pin, mode
adc = ADC(Pin(26, mode=Pin.IN))

def map_to_rainbow_color(value):
    # Map the potentiometer value to the range of rainbow colors and names
    if value > 0 and value < 300:
        return (255, 0, 0), "Red"
    elif value > 301 and value < 600:
        return (255, 127, 0), "Orange"
    elif value > 601 and value < 900:
        return (255, 255, 0), "Yellow"
    elif value > 901 and value < 1200:
        return (0, 255, 0), "Green"
    elif value > 1201 and value < 1500:
        return (0, 0, 255), "Blue"
    elif value > 1501 and value < 1800:
        return (75, 0, 130), "Indigo"
    elif value > 1801 and value < 2100:
        return (148, 0, 211), "Violet"
    else:
        return (0, 0, 0), "Unknown"  # Default case if value is outside range

while True:
    duty = adc.read_u16() #between ~350-65535
    low_res = duty >> 5
    color, color_name = map_to_rainbow_color(int(low_res))
    pixels.set_pixel(0, color)
    pixels.show()
    time.sleep_ms(100)

    if not button.value():
        print("button pressed")
        print("Potentiometer Value:", low_res)
        print("Color Hex:", '#%02x%02x%02x' % color)
        print("Color Name:", color_name)
        time.sleep_ms(200)
