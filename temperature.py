from microbit import temperature, display

while True:
    if temperature() > 30:
        display.scroll("ALERT!!")
    display.scroll(str(temperature()) + " °C")