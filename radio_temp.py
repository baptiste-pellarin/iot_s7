import radio
from microbit import display, temperature, button_a

radio.config(channel=69, address=0x75626969)
radio.on()

while True:

    if button_a.was_pressed():
        radio.send('C'+str(temperature()))
        print('temperature envoyée')

    incoming = radio.receive()
    if incoming and incoming[0] == "C":
        print("incoming", incoming)

        print("Local", str(temperature()), "°C")
        print("Ext", incoming[1:], "°C")

