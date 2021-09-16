import radio
from microbit import display, sleep, temperature

"""
Master (delta temp)
"""

radio.config(channel=69, address=0x75626969)
radio.on()

while True:

    sleep(500)

    incoming = radio.receive()
    if incoming and incoming[0] == "C":
        print("incoming", incoming)

        print("Local", str(temperature()), "°C")
        print("Ext", incoming[1:], "°C")

