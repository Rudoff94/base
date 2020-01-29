#include "Motor.h"
Motor motors[2];
void setup()
{
  motors[0].setup(5, 6);
  motors[1].setup(9, 10);
  //motors[1].setMotor(1, 255);
  motors[0].setMotor(1, 255);
  delay(1000);
  //motors[1].setMotor(1, 0);
  motors[0].setMotor(1, 0);
  Serial.begin(9600);

}

void loop()
{
  if (Serial.available() > 2)
  {
    int num_of_motor = Serial.read() - 48;
    int dir = Serial.read() - 48;
    int power = Serial.read();
        if ((num_of_motor < 2) && (num_of_motor > -1))
        {
          Serial.println("OK");
          motors[num_of_motor].setMotor(dir, power);
        }
    Serial.print(num_of_motor);
    Serial.print(' ');
    Serial.print(dir);
    Serial.print(' ');
    Serial.println(power);
  }
}
