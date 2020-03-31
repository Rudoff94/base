#!/usr/bin/env python
import rospy
from rpi_platform_ros.msg import BaseMotorControl
from time import sleep

def main():
	rospy.init_node('Test_node')
	pub = rospy.Publisher('base/motor_control',BaseMotorControl, queue_size = 5)
	sleep(1)
	msg = BaseMotorControl()
	msg.motor = 0
	msg.direction = 0

	while not rospy.is_shutdown():
		msg.power = 20
		pub.publish(msg)
		sleep(3)
		msg.power = 0
		pub.publish(msg)
		sleep(3)

if __name__ == '__main__':
	main()
