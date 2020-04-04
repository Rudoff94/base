#!/usr/bin/env python
import rospy
from rpi_platform_ros.msg import BaseMotorControl
from time import sleep
import socket
import struct
from constants import *

def main():
	rospy.init_node('Test_node')
	#server init
	host = '192.168.2.108'
	port = 2002
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((host, port))
	server.listen(2)
	rospy.loginfo('GAMEPAD_SERVER starting..')
	#init publisher
	pub = rospy.Publisher('base/motor_control',BaseMotorControl, queue_size = 5)
	sleep(1)
	msg_left_motor = BaseMotorControl()
	msg_left_motor.motor = ArduinoCommand.MOTOR_L
	msg_left_motor.direction = ArduinoCommand.FORWARD
	msg_left_motor.power = 0
	msg_right_motor = BaseMotorControl()
	msg_right_motor.motor = ArduinoCommand.MOTOR_R
	msg_right_motor.direction = ArduinoCommand.FORWARD
	msg_right_motor.power = 0

	def stop_platform():
		msg_right_motor.power = 0
		msg_left_motor.power = 0
		pub.publish(msg_right_motor)
		pub.publish(msg_left_motor)

	#init closing
	def close():
		server.close()
		rospy.loginfo('GAMEPAD_SERVER: stop server')
		stop_platform()	
	rospy.on_shutdown(close)
	while not rospy.is_shutdown():
		try:
			conn, addr = server.accept()
			rospy.loginfo('GAMEPAD_SERVER: connected to' + str(addr))
			while conn:
				len_pack = conn.recv(1)
				len_pack = struct.unpack('B', len_pack)[0]
				pack = conn.recv(len_pack)
				pack_int = []
				for bt in pack:
					pack_int.append(struct.unpack('B', bt)[0] - 100)
				rospy.loginfo('Received data: ' + str(pack_int))
				
				#left_motor
				if pack_int[1] > 0:
					msg_left_motor.direction = ArduinoCommand.FORWARD
					msg_left_motor.power = pack_int[1]
				else:
					msg_left_motor.direction = ArduinoCommand.BACKWARD
					msg_left_motor.power = -1 * pack_int[1]					
				if pack_int[3] < 0:
					msg_right_motor.direction = ArduinoCommand.FORWARD
					msg_right_motor.power = -1 * pack_int[3]
				else:
					msg_right_motor.direction = ArduinoCommand.BACKWARD
					msg_right_motor.power = pack_int[3]
				pub.publish(msg_right_motor)
				pub.publish(msg_left_motor)



		except socket.error:
			rospy.loginfo('GAMEPAD_SERVER:Lost connection')
			stop_platform()
		except struct.error:
			rospy.loginfo('GAMEPAD_SERVER:Lost connection')
			stop_platform()
		except KeyboardInterrupt:
			close()
			return
		
if __name__ == '__main__':
	main()
