#include "motordriver_4wd.h"
#include <seeed_pwm.h>

void setup() {
  MOTOR.init();

}

void loop() {

 MOTOR.setSpeedDir2(65, DIRF);
 MOTOR.setSpeedDir1(0, DIRR);
 delay(2000);
  MOTOR.setSpeedDir2(0, DIRF);
  MOTOR.setSpeedDir1(65, DIRF);
  delay(2000);
  MOTOR.setSpeedDir2(65, DIRR);
  MOTOR.setSpeedDir1(0, DIRR);
  delay(2000);
  MOTOR.setSpeedDir2(0, DIRF);
  MOTOR.setSpeedDir1(65, DIRR);
  delay(2000);

}
