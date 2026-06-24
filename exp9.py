import RPi.GPIO as GPIO
import requests
import time

LDR_PIN = 17
LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LDR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

API_KEY = "your_write_api_key"
URL = "https://api.thingspeak.com/update"

try:
	while True:
		ldr_value = GPIO.input(LDR_PIN)
		if ldr_value == 0:
			GPIO.output(LED_PIN, GPIO.HIGH)
			light_status = "ON"
			print("Dark Detected\nLED ON")
		else:
			GPIO.output(LED_PIN, GPIO.LOW)
			light_status = "OFF"
			print("Bright Detected\nLED OFF")
		payload = {
			"api_key": API_KEY,
			"field1" : ldr_value,
			"field2" : 1 if light_status == "ON" else 0
		}
		try:
			response = requests.get(URL, params = payload)
			if response.status_code == 200:
				print("Data uploaded to ThingSpeak")
			else:
				print("Upload Failed")
		except Exception as e:
			print("Internet Error:", e)
except KeyboardInterrupt:
	GPIO.cleanup()
	print("Program Stopped")			
