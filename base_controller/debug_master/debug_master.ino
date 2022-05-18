#include <SoftwareSerial.h>
SoftwareSerial debugSerial(2, 3);

void setup() {
  Serial.begin(9600);
  debugSerial.begin(9600);

}

void loop() {
  if(Serial.available()) {
    char input = Serial.read();
    debugSerial.print(input);
  }

}
