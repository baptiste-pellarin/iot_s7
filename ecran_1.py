from ssd1306_bitmap import show_bitmap
from ssd1306 import initialize, clear_oled
from microbit import sleep, pin0


initialize(pinReset = pin0)
#clear_oled()

show_bitmap("ledemon")