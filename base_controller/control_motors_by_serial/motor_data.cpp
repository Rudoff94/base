#include "motor_data.h"

MotorData::MotorData() {
    numberOfMotor = 0;
    direction = 0;
    speed = 0;
}
 bool MotorData::parseBuffer(uint8_t* buffer, uint8_t bufferSize){
    if(bufferSize != 3) return false;
    numberOfMotor = *buffer;
    direction = (bool)*(buffer + 1);
    speed = *(buffer + 2);
    return true;
 }

uint8_t MotorData::getNumberOfMotor() {
    return numberOfMotor;
}

uint8_t MotorData::getMotorSpeed() {
    return speed;
}

bool MotorData::getMotorDirection() {
    return direction;
}