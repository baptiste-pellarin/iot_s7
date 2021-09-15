from microbit import display, compass, button_a, Image


while True:

    while not compass.is_calibrated() or button_a.is_pressed():
        compass.clear_calibration()
        compass.calibrate()
        display.scroll("C")
    needle = ((15 - compass.heading()) // 30) % 12
    display.show(Image.ALL_CLOCKS[needle])
