#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2); // Try 0x27 or 0x3F if not working

int pulsePin = A0;
int threshold = 550;

int bpm = 0;
int beatCount = 0;

unsigned long lastBeatTime = 0;
unsigned long lastCalcTime = 0;

void setup() {
  lcd.init();
  lcd.backlight();

  pinMode(pulsePin, INPUT);

  lcd.setCursor(0, 0);
  lcd.print("Heart Rate");
  delay(2000);
  lcd.clear();
}

void loop() {
  int signal = analogRead(pulsePin);

  if (signal > threshold) {
    unsigned long currentTime = millis();

    if (currentTime - lastBeatTime > 300) { // debounce
      beatCount++;
      lastBeatTime = currentTime;
    }
  }

  // Calculate BPM every 10 seconds
  if (millis() - lastCalcTime >= 10000) {
    bpm = beatCount * 6;
    beatCount = 0;
    lastCalcTime = millis();

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("BPM:");

    lcd.setCursor(0, 1);
    lcd.print(bpm);
    lcd.print(" bpm");
  }
}

