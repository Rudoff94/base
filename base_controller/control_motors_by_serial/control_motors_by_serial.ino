#include "motordriver_4wd.h"
#include <seeed_pwm.h>
#include "communication protocol.h"
#include "motor_data.h"
#include <String.h>

#define DEBUG_RX 2
#define DEBUG_TX 3
//#define DEBUG

#ifdef DEBUG
#define BAUDRATE 9600
#else
#define BAUDRATE 115200
#endif

SoftwareSerial debugSerial(DEBUG_RX, DEBUG_TX);
CommunicationProtocol commProtocol;
MotorData motorData;

void setMotorSpeed(MotorData& motorData);

void setup() {
  MOTOR.init();
  Serial.begin(BAUDRATE);
  debugSerial.begin(9600);
#ifdef DEBUG
  commProtocol.initDebug(&debugSerial);
#endif
}


void loop() {

  if (commProtocol.available()) {
    commProtocol.read();
    uint8_t* buffAddr = commProtocol.getBuffer();
    uint8_t buffSize = commProtocol.getBufferSize();
    if (motorData.parseBuffer(buffAddr, buffSize)) {
      setMotorSpeed(motorData);
    }
  }
}

void setMotorSpeed(MotorData& motorData) {
  if (motorData.getNumberOfMotor() == LEFT_MOTOR) {
    MOTOR.setSpeedDir2(motorData.getMotorSpeed(), motorData.getMotorDirection());
  }
  else if (motorData.getNumberOfMotor() == RIGHT_MOTOR) {
    MOTOR.setSpeedDir1(motorData.getMotorSpeed(), !motorData.getMotorDirection());
  }
}
