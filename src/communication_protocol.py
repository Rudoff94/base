class CommunicationProtocolMessage:

    def __init__(self):
        self.start_byte = 0x48 #72
   
    def pack(self, data):
        return bytes(bytearray([self.start_byte, len(data)] + data))

# import serial
# import time

# msg = CommunicationProtocolMessage()
# data1 = msg.pack([2,1, 50])
# print(data1)
# data3 = msg.pack([2,1,0])
# print(data3)

# data2 = msg.pack([1,1])
# print(data2)
# data4 = msg.pack([1,1,0])
# print(data4)

# com_port = serial.Serial('COM7', 115200)
# com_port.write(data2)
# com_port.write(data1)
# time.sleep(2)
# com_port.write(data4)
# com_port.write(data3)

