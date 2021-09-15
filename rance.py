"""
    neopixel_random.py

    Repeatedly displays random colours onto the LED strip.
    This example requires a strip of 8 Neopixels (WS2812) connected to pin0.

"""
from microbit import sleep, pin0
import neopixel

# Setup the Neopixel strip on pin0 with a length of 8 pixels
np = neopixel.NeoPixel(pin0, 1)

while True:
    #Iterate over each LED in the strip
    np[0] = (0, 0, 255)
    np.show()
    sleep(250)
    np[0] = (255, 255, 255)
    np.show()
    sleep(250)
    np[0] = (255, 0, 0)
    np.show()
    sleep(250)

