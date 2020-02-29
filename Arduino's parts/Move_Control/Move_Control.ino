#include "Motor.h"
Motor motors[2];
void setup()
{
  motors[0].setup(5, 6);
  motors[1].setup(9, 10);
Serial.begin(9600);

}

void loop()
{
  if (Serial.available() > 2)
  {
    uint8_t num_of_motor = Serial.read();
    uint8_t dir = Serial.read();
    uint8_t power = Serial.read();
    if ((num_of_motor < 2) && (num_of_motor > -1))
    {
      motors[num_of_motor].setMotor(dir, power);
    }
    Serial.write(num_of_motor);
    Serial.write(dir);
    Serial.write(power);
    /*Serial.print(num_of_motor);
    Serial.print(dir);
    Serial.println(power);*/
  }
}
