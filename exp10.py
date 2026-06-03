import RPi.GPIO as GPIO
import time
import smtplib
from email.mime.text import MIMEText
SENSOR_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"
TO_EMAIL = "receiver_email@gmail.com"
def send_email(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL
    msg['To'] = TO_EMAIL
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Email sent:", subject)
    except Exception as e:
        print("Error:", e)
print("Monitoring soil moisture...")
dry_alert_sent = False
wet_alert_sent = False
try:
    while True:
        moisture = GPIO.input(SENSOR_PIN)
        if moisture == 1:
            print("Soil is DRY")
            if not dry_alert_sent:
                send_email("Soil Dry Alert 🌱", "The soil is dry. Please water the plant.")
                dry_alert_sent = True
                wet_alert_sent = False
        else:
            print("Soil is WET")
            if not wet_alert_sent:
                send_email("Soil Wet Update 💧", "Soil moisture is sufficient.")
                wet_alert_sent = True
                dry_alert_sent = False
        time.sleep(5)
except KeyboardInterrupt:
    print("Stopped")
finally:
    GPIO.cleanup()