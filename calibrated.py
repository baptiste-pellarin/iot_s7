from microbit import display, accelerometer, button_a

i = 0

while True:
    if button_a.is_pressed():
        compass.calibrate()
        display.scroll("C")

    if accelerometer.current_gesture() == "left":
        i += 1
        display.scroll(i)