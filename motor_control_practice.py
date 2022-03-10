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

# 3. CONTROL
try :
    while True :
        p.ChangeDutyCycle(5)
        time.sleep(1)
        p.ChangeDutyCycle(10)
        time.sleep(1)
except KeyboardInterrupt :
    p.stop()

# 4. CLEANUP
GPIO.cleanup()
