#ifndef MOTOR_DATA
#define MOTOR_DATA

#include <Arduino.h>

#define LEFT_MOTOR 0x01
#define RIGHT_MOTOR 0x02


class MotorData {
private:
    uint8_t numberOfMotor;
    bool direction;
    uint8_t speed;
public:
    MotorData();
    bool parseBuffer(uint8_t* buffer, uint8_t bufferSize);
    uint8_t getNumberOfMotor();
    uint8_t getMotorSpeed();
    bool getMotorDirection();
};


#endif //MOTOR_DATA