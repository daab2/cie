import RPi.GPIO as GPIO
import smtplib
from email.mime.text import MIMEText
import time

# -------------------------------
# GPIO SETUP
# -------------------------------
SENSOR_PIN = 17   # Change if needed

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# -------------------------------
# EMAIL CONFIG
# -------------------------------
EMAIL_SENDER = "abc"
EMAIL_PASSWORD = "xyz"   # Use App Password (important!)
EMAIL_RECEIVER = "abc"

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# -------------------------------
# SEND EMAIL FUNCTION
# -------------------------------
def send_email(message):
    try:
        msg = MIMEText(message)
        msg["Subject"] = "Water Level Alert"
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        print("Email sent successfully!")

    except Exception as e:
        print("Error sending email:", e)

# -------------------------------
# MAIN LOOP
# -------------------------------
last_state = None

try:
    while True:
        state = GPIO.input(SENSOR_PIN)

        if state != last_state:
            if state == 1:
                print("Water Level HIGH")
                send_email("Alert: Water level is HIGH ⚠️")
            else:
                print("Water Level LOW")
                send_email("Alert: Water level is LOW ⚠️")

            last_state = state

        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()

