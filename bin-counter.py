import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]
num = 0
sleep_time = 0.2

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

GPIO.setup(9, GPIO.IN)
GPIO.setup(10, GPIO.IN)

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

while True:
    if GPIO.input(9):
        num = num + 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(10):
        num = num - 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if num < 0 or num == 256:
        break
    GPIO.output(leds, dec2bin(num))
