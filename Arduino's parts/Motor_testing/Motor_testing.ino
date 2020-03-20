#include "Motor.h"
Motor motors[2];
void setup()
{
  motors[0].setup(5, 6);
  motors[1].setup(9, 10);
}

void loop()
{
  motors[0].setMotor(0, 255);
  motors[1].setMotor(0, 255);
  delay(2000);
  motors[0].setMotor(0, 0);
  motors[1].setMotor(0, 0);
  while(true);
}
