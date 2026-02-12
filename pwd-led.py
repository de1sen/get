import RPi.GPIO as GPIO
import time

led = 26
duty = 0.0

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

pwm = GPIO.PWM(led, 200)
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)

    duty += 1.0
    if duty > 100.0:
        duty = 0.0

