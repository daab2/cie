import RPi.GPIO as GPIO
import time

PIR_PIN = 17   # PIR OUT pin
LED_PIN = 27   # LED pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

print("Waiting for PIR sensor to settle...")
time.sleep(5)  # Sensor calibration time

try:
    while True:
        motion = GPIO.input(PIR_PIN)

        if motion:
            print("Motion detected!")
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            print("No motion")
            GPIO.output(LED_PIN, GPIO.LOW)

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Program stopped")

finally:
    GPIO.cleanup()

