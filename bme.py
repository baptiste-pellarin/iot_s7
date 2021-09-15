from bme280 import bme280
from microbit import sleep

b = bme280()
while True:
    t, p, h, a = b.all()
    print("T: {t}, P: {p}, H: {h}, A: {a}".format(t=t,p=p,h=h,a=a))
    sleep(1000)