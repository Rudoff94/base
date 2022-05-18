#ifndef COMM_PROTOCOL
#define COMM_PROTOCOL

// #include <Serial.h>
#include "Arduino.h"
#include <SoftwareSerial.h>


#define MAX_BUF_SIZE 50
#define START_BYTE 0x48

class CommunicationProtocol {
private:
    const SoftwareSerial* debugSerial;
    uint8_t buffer[MAX_BUF_SIZE];
    uint8_t bufferSize;
    bool validate();
    void printBuffer();
    uint8_t readMessageFailed();

public:
    CommunicationProtocol();
    bool available();
    uint8_t read();
    uint8_t* getBuffer();
    uint8_t getBufferSize();
    void clearBuffer();
    void initDebug(const SoftwareSerial* softwareSerial);
};


#endif //COMM_PROTOCOL