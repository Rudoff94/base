class MotorData:
    def __init__(self):
        pass

    def pack(self, motor_number, direction, speed):
        return list([motor_number, direction, speed])
