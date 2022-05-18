#!/usr/bin/env python
import rospy
import cv2
import socket
import numpy
from time import sleep

def main():
	rospy.init_node('cam_server')
	cam = cv2.VideoCapture(0)
	HOST = '192.168.0.106'
	PORT = 2000
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	server.bind((HOST, PORT))
	server.listen(2)
	rospy.loginfo('Starting server...')
	try:
		while True:
			conn, addr = server.accept()
			if conn:
				rospy.loginfo('Connected by' + str(addr))
			try:
				while conn:
					ret, frame = cam.read()
					if ret:
						frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
						frame = cv2.resize(frame.astype(numpy.uint8), (227,227),interpolation=cv2.INTER_CUBIC)	
						length = frame.shape[0] * frame.shape[1]
						conn.sendall(str(length))
						rospy.loginfo('msg_len: '+ str(length))
						conn.sendall(frame)
					else:
						rospy.loginfo('Camera error')
			except socket.error:
				rospy.loginfo('Lost connection')
			except KeyboardInterrupt:
				raise KeyboardInterrupt
	except KeyboardInterrupt:
		rospy.loginfo('Stop server')
		server.close()
	rospy.loginfo('Camera release')
	cam.release()

if __name__ == "__main__":
	main()
	


