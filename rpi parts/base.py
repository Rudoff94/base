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
		patern = r'ttyUSB[0-9]'

		for cur_dev in dev_list:
			if re.match(patern, cur_dev):
				print("Device: ", cur_dev)
				self.arduino = serial.Serial('/dev/' + cur_dev, self.speed)
				return True
		self.arduino = None
		print("Cannot find Arduino at list... ")
		return False

	def set_motor(self, motor, dir, power):
		if self.arduino is not None:
			if (motor >= ArduinoCommand.MOTOR_L and motor <= ArduinoCommand.MOTOR_R):
				if (dir >= ArduinoCommand.BACKWARD and dir <= ArduinoCommand.FORWARD):
					if (power >= ArduinoCommand.MINPOWER and power <= ArduinoCommand.MAXPOWER): 
						#Проблема была в кодировке
						#Для того, чтобы перевести число в байт: bytes([число])
						message = [bytes([motor]), bytes([dir]), bytes([power])]
						for i in message:
							self.arduino.write(i)
			print("Error in formating package")
			return False
		print("Arduino isn't connected")
		return False