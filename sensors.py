from microbit import temperature, sleep, button_a, button_b, display, accelerometer, compass
compass.calibrate()

while True:
    if button_a.get_presses():
        print("Btn A pressed")
        print(temperature(), "°C")

    elif button_b.get_presses():
        print("Btn B pressed")
    else:
        print("compass")
        print(str(compass.heading()))
        print("light")
        print(display.read_light_level())
        print("accelerometer gestures")
        print(accelerometer.get_gestures())

    sleep(500)