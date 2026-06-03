from flask import Flask, render_template
import threading
import sensor

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("main.html",
                           temperature=sensor.temperature,
                           humidity=sensor.humidity)

def run_sensor():
    sensor.sensor_loop()


if __name__ == "__main__":
    try:
        sensor_thread = threading.Thread(target = run_sensor)
        sensor_thread.daemon = True
        sensor_thread.start()

        # Start web server
        app.run(host="0.0.0.0", port=5000, debug=False)

    except KeyboardInterrupt:
        print("Shutting down...")
