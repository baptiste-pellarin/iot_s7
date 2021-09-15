from microbit import pin8, pin12, pin16, sleep

timer = 3000

while True:
    sleep(timer)
    pin16.write_digital(0)
    pin8.write_digital(1)
    sleep(timer)
    pin8.write_digital(0)
    pin12.write_digital(1)
    sleep(timer/2)
    pin12.write_digital(0)
    pin16.write_digital(1)

