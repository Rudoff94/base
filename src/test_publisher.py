#!/usr/bin/env python
import rospy
from rpi_platform_ros.msg import BaseMotorControl
from time import sleep
import socket
import struct

def

def main():
	rospy.init_node('Test_node')
	#server init
	host = '192.168.2.108'
	port = 2002
	server = socket.socket(AF_INET, socket.SOCK_STREAM)
	server.bind((host, port))
	server.listen(2)
	rospy.loginfo('GAMEPAD_SERVER starting..')
	#init publisher
	pub = rospy.Publisher('base/motor_control',BaseMotorControl, queue_size = 5)
	sleep(1)
	msg = BaseMotorControl()

	while True:
		
'''
	while not rospy.is_shutdown():
		msg.motor = 0
		msg.direction = 0
		msg.power = 50
		pub.publish(msg)
		msg.motor = 1
		msg.direction = 1
		msg.power = 50
		pub.publish(msg)
		sleep(1)
		msg.motor = 0
		msg.direction = 1
		msg.power = 50
		pub.publish(msg)
		msg.motor = 1
		msg.direction = 0
		msg.power = 50
		pub.publish(msg)
		sleep(1)
		msg.motor = 0
		msg.direction = 1
		msg.power = 0
		pub.publish(msg)
		msg.motor = 1
		msg.direction = 1
		msg.power = 0
		pub.publish(msg)
		sleep(2)
'''
if __name__ == '__main__':
	main()
