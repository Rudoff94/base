#include "communication protocol.h"

CommunicationProtocol::CommunicationProtocol() {
    bufferSize = 0;
    debugSerial = NULL;
}

void  CommunicationProtocol::initDebug(const SoftwareSerial* softwareSerial) {
    debugSerial = softwareSerial;
}

bool CommunicationProtocol::validate() {
    return true; 
}

bool CommunicationProtocol::available() {
    return Serial.available() > 1;
}

uint8_t CommunicationProtocol::read() {
    //check start byte
    clearBuffer();
    buffer[0] = (uint8_t)Serial.read();
    bufferSize++;
    if(buffer[0] != START_BYTE) readMessageFailed();
 
    //check length of data
    uint8_t messageLength = (uint8_t)Serial.read();
    buffer[1] = messageLength;
    bufferSize++;
    if(messageLength > MAX_BUF_SIZE) readMessageFailed();
    
    size_t readSize = Serial.readBytes(buffer + 2,messageLength);
    bufferSize += readSize;
    if(readSize != messageLength ) readMessageFailed();

    if(!validate()) readMessageFailed();

    printBuffer();
    return bufferSize;
}

uint8_t* CommunicationProtocol::getBuffer(){
    return buffer + 2;
}

uint8_t CommunicationProtocol::getBufferSize() {
    return bufferSize - 2;
}

void CommunicationProtocol::clearBuffer() {
    bufferSize = 0;
}

void CommunicationProtocol::printBuffer() {
    if(debugSerial == NULL) return;
    for(int index = 0; index < bufferSize; index++) {
        debugSerial->print(buffer[index]);
        debugSerial->print(' ');
    }
    debugSerial->println();
}

uint8_t CommunicationProtocol::readMessageFailed() {
    printBuffer();
    clearBuffer();
    return 0;
}
