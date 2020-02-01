import re
import os
import serial
from constants import ArduinoCommand

class Base:
	def __init__(self):
		self.arduino = None
		self.speed = 9600

	def find_arduino(self):
		dev_list = os.listdir('/dev')
		patern = r'/dev/ttyUSB[0-9]'

		for cur_dev in dev_list:
			if cur_dev == patern:
				print("Device: ", cur_dev)
				self.arduino = serial.Serial('/dev/ttyUSB0', self.speed)
				return True
		self.arduino = None
		print("Cannot find Arduino at list... ")
		return False

	def set_motor(self, motor, dir, power):
		if self.arduino is not None:
			if (motor >= ArduinoCommand.MOTOR_L and motor <= ArduinoCommand.MOTOR_R):
				if (dir >= ArduinoCommand.BACKWARD and dir <= ArduinoCommand.FORWARD):
					if (power >= ArduinoCommand.MINPOWER and power <= ArduinoCommand.MAXPOWER): 
						message = [motor, dir, power]
						for i in message:
							self.arduino.write(i)
			print("Error in formating package")
			return False
		print("Arduino isn't connected")
		return False