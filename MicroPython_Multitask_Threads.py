import _thread
from time import sleep
from machine import Pin

led = Pin(2, Pin.OUT)


def blink_led():
    led.value(0)
    sleep(1)
    led.value(1)
    sleep(1)


def blink_forever():
    while True:
        blink_led()


_thread.start_new_thread(blink_forever, ())

while True:
    print("hello world")
    sleep(2)





