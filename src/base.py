#!/usr/bin/env python
import re
import os
import serial
from constants import ArduinoCommand
import rospy
from rpi_platform_ros.msg import BaseMotorControl
from time import sleep
class Base:

	def __init__(self):
		rospy.init_node('base_node')
		self.arduino = None
		self.speed = 9600
		rospy.on_shutdown(self.close)
		#add topic - control base
		self.motor_data_sub = rospy.Subscriber("base_motor_control", BaseMotorControl, self.handler_motor_data)
	
	def handler_motor_data(self, motor_data):
		print(motor_data)
		self.set_motor(motor_data.motor, motor_data.direction, motor_data.power)


	def loop(self):
		while not rospy.is_shutdown():
			while not rospy.is_shutdown():
				if self.find_arduino():
					break
				sleep(1)
			while not rospy.is_shutdown():
				if self.arduino == None:
					break
				sleep(1)

	def find_arduino(self):
		dev_list = os.listdir('/dev')
		patern = r'ttyUSB[0-9]'

		for cur_dev in dev_list:
			if re.match(patern, cur_dev):
				print("Connected to device: ", cur_dev)
				self.arduino = serial.Serial('/dev/' + cur_dev, self.speed)
				return True
		self.arduino = None
		print("Cannot find Arduino at list... ")
		return False

	def set_motor(self, motor, dir, power):
		try:
			if self.arduino !=  None:
				msg = bytes(bytearray([motor, dir, power]))
				#print(msg)
				self.arduino.write(msg)
		except serial.SerialException:
			self.arduino.close()
			self.arduino = None
			print("Arduino isn't connected")
		
	def close(self):
		if self.arduino != None:
			self.arduino.close()

def main():
	base = Base()
	base.loop()

if __name__ == '__main__':
	main()
