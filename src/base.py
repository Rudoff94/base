import re
import os
import serial
from constants import ArduinoCommand
import rospy

class Base:
	def __init__(self):
		rospy.init('base_node')
		self.arduino = None
		self.speed = 9600
		rospy.on_shutdown(self.close)
		#add topic - control base

	def loop():
		while True:
			while not rospy.is_shutdown():
				if self.find_arduino():
					break
			while not rospy.is_shutdown():
				pass

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

	def close(self):
		if self.arduino != None:
			self.arduino.close()

def main():
	base = Base()
	base.loop()
