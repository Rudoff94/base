#!/usr/bin/env python
import re
import os
import serial
from motor_data import MotorData
from communication_protocol import CommunicationProtocolMessage
from constants import ArduinoCommand
import rospy
from rpi_platform_ros.msg import BaseMotorControl
from std_msgs.msg import Bool
from time import sleep

class Base:

	def __init__(self):
		rospy.init_node('base_node')
		self.arduino = None
		self.speed = 115200
		self.connection = False
		rospy.on_shutdown(self.close)
		#add topic - control base
		self.motor_data_sub = rospy.Subscriber("base/motor_control", BaseMotorControl, self.handler_motor_data)
		self.connection_status_pub = rospy.Publisher("base/connection", Bool, queue_size=5)

	def handler_motor_data(self, motor_data):
		print(motor_data)
		self.set_motor(motor_data.motor, motor_data.direction, motor_data.power)


	def loop(self):
		rate = rospy.Rate(10)
		while not rospy.is_shutdown():
			if self.arduino == None:
				self.find_arduino()
			self.connection_status_pub.publish(self.connection)
			rate.sleep(0)

	def find_arduino(self):
		dev_list = os.listdir('/dev')
		patern = r'ttyUSB[0-9]'

		for device in dev_list:
			if re.match(patern, device):
				print("Connected to device: ", device)
				self.arduino = serial.Serial('/dev/' + device, self.speed)
				self.connection = True
				return True
		print("Cannot find Arduino at list... ")
		return False

	def set_motor(self, motor_number, dir, power):
		'''
			motor: 0x00 - LEFT, 0x01 - RIGHT
			direction: 0x00 - FORWARD, 0x01 - REVERSE
			power: 0 - 100
		'''
		try:
			if self.arduino !=  None:
				#msg = bytes(bytearray([self.prefix, motor, dir, power]))
				motorData = MotorData()
				protocolMsg = CommunicationProtocolMessage()
				msg = protocolMsg.pack(motorData.pack(motor_number, dir, power))
				print(msg)
				self.arduino.write(msg)
		except serial.SerialException:
			self.arduino.close()
			self.arduino = None
			self.connection = False
			print("Arduino isn't connected")
		
	def close(self):
		if self.arduino != None:
			self.arduino.close()

def main():
	base = Base()
	base.loop()

if __name__ == '__main__':
	main()
