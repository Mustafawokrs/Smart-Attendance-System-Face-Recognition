// Pins configuration as per Technical Report
const int greenLed = 12; // For "Present" 
const int redLed = 13;   // For "Unrecognized" 
const int buzzer = 11;   // Audio signal [cite: 15]

void setup() {
  Serial.begin(9600); // Communication via PySerial [cite: 10]
  pinMode(greenLed, OUTPUT);
  pinMode(redLed, OUTPUT);
  pinMode(buzzer, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    if (command == 'P') { // Success: Present [cite: 22]
      digitalWrite(greenLed, HIGH);
      digitalWrite(buzzer, HIGH);
      delay(800);
      digitalWrite(greenLed, LOW);
      digitalWrite(buzzer, LOW);
    } 
    else if (command == 'U') { // Failure: Unrecognized 
      digitalWrite(redLed, HIGH);
      digitalWrite(buzzer, HIGH);
      delay(200); // Short bursts for error sound
      digitalWrite(buzzer, LOW);
      delay(100);
      digitalWrite(buzzer, HIGH);
      delay(200);
      digitalWrite(redLed, LOW);
      digitalWrite(buzzer, LOW);
    }
  }
}