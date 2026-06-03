
#include <MPU6050.h>

MPU6050 mpu;

int16_t ax, ay, az;

void setup() {
  Serial.begin(9600);
  mpu.initialize();
}

void loop() {
  // Read accelerometer data
  mpu.getAcceleration(&ax, &ay, &az);

  // Convert to g (optional scaling)
  float Ax = ax / 16384.0;
  float Ay = ay / 16384.0;
  float Az = az / 16384.0;

  // Calculate tilt angles (in degrees)
  float pitch = atan2(Ax, sqrt(Ay * Ay + Az * Az)) * 180.0 / PI;
  float roll  = atan2(Ay, sqrt(Ax * Ax + Az * Az)) * 180.0 / PI;

  // Print results
  Serial.print("Pitch: ");
  Serial.print(pitch);
  Serial.print(" | Roll: ");
  Serial.println(roll);

  delay(500);
}

