import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

ledPin = 7

try:
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setup(ledPin, GPIO.OUT) ## Setup GPIO Pin 7 to OUT	

    while True:
        GPIO.output(ledPin, 1)
        time.sleep(1)
        GPIO.output(ledPin, 0)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
