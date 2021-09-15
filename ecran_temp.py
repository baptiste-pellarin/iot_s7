from ssd1306 import initialize, clear_oled
from microbit import sleep, pin0
from bme280_light import bme280
from ssd1306_text import add_text


initialize(pinReset = pin0)
clear_oled()

add_text(1, 1, "Init...")


sleep(1000)
bme = bme280()

while True:

    temp = str(bme.temperature()) + " C"

    add_text(1, 1, temp)
    sleep(500)

