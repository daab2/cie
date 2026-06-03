import adafruit_dht
import board
import time

dhtDevice = adafruit_dht.DHT11(board.D4)

# Shared data
temperature = 0
humidity = 0

def sensor_loop():
    global temperature, humidity

    while True:
        try:
            temp = dhtDevice.temperature
            hum = dhtDevice.humidity

            if temp is not None and hum is not None:
                temperature = round(temp, 1)
                humidity = round(hum, 1)
                print(f"Temp={temperature}°C  Humidity={humidity}%")

        except RuntimeError:
            # DHT11 glitch fix
            pass

        except Exception as e:
            dhtDevice.exit()
            raise e

        time.sleep(2)
