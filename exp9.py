import spidev
import time
import RPi.GPIO as GPIO
import requests

# -------------------------------
# GPIO SETUP
# -------------------------------
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# -------------------------------
# SPI (MCP3008) SETUP
# -------------------------------
spi = spidev.SpiDev()
spi.open(0, 0)   # Bus 0, Device 0
spi.max_speed_hz = 1350000

def read_adc(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

# -------------------------------
# CLOUD (ThingSpeak)
# -------------------------------
API_KEY = "YOUR_API_KEY"
URL = "https://api.thingspeak.com/update"

# -------------------------------
# THRESHOLD
# -------------------------------
THRESHOLD = 400   # Adjust after testing

# -------------------------------
# MAIN LOOP
# -------------------------------
try:
    while True:
        light_level = read_adc(0)   # Channel 0

        # Light control
        if light_level < THRESHOLD:
            GPIO.output(LED_PIN, GPIO.HIGH)
            status = 1   # Light ON
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            status = 0   # Light OFF

        print(f"LDR Value: {light_level} | LED: {status}")

        # Send to cloud
        payload = {
            "api_key": API_KEY,
            "field1": light_level,
            "field2": status
        }

        try:
            requests.get(URL, params=payload)
        except:
            print("Cloud update failed")

        time.sleep(15)   # ThingSpeak limit

except KeyboardInterrupt:
    GPIO.cleanup()
    spi.close()

