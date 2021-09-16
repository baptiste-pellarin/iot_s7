import radio
from microbit import display, button_a, sleep

radio.config(channel=69, address=0x75626969)
radio.on()

while True:

    if button_a.was_pressed():
        radio.send('PELLARIN à KHETTAL')  # a-ha
        print("Msg Sended")

    incoming = radio.receive()
    if incoming:
        print("incoming", incoming)