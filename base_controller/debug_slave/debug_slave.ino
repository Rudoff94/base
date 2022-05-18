#include <SoftwareSerial.h>
SoftwareSerial debugSerial(4, 5);

void setup() {
  Serial.begin(9600);
  debugSerial.begin(9600);

}

void loop() {
  if(debugSerial.available()) {
    char input = debugSerial.read();
    Serial.print(input);
  }

}
