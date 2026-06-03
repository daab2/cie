// Define pins
const int smokeSensor = A0;  // MQ-2 analog output
const int buzzerPin = 9;     // Buzzer pin

// Threshold value (adjust this!)
int threshold = 800;

void setup() {
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(smokeSensor);

  Serial.print("Smoke Level: ");
  Serial.println(sensorValue);

  // If smoke detected
  if (sensorValue > threshold) {
    digitalWrite(buzzerPin, HIGH); // Turn buzzer ON
  } else {
    digitalWrite(buzzerPin, LOW);  // Turn buzzer OFF
  }

  delay(200);
}
