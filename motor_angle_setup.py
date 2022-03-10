# Raspberry pi 4 + Ubuntu 20.04 + python3
# Servomotor MG 946R & MG 995 at pin number 03

import time
from time import sleep
import RPi.GPIO as GPIO

# 1. PIN NO. SET
servoPIN = 3
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(servoPIN, GPIO.OUT, initial=GPIO.HIGH)

# 2. PWM SET
p = GPIO.PWM(servoPIN, 50)
p.start(5)

# 3. SET ANGLE
def setAngle(angle) :
    duty = angle / 18 + 2
    GPIO.output(servoPIN, True)
    p.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(servoPIN, False)
    p.ChangeDutyCycle(0)

setAngle(90) # set angle to 90 degrees

p.stop()

# 4. CLEAN UP
GPIO.cleanup()