from base import Base
from constant import ArduinoCommand as ac
from time import sleep
from detect_black_object import get_signature
from pid import PID
import cv2
import numpy as np

def main():
	#Variables for PID
	kp = 
	kd = 
	ki = 
	min = 0
	max = 255

	#Variables for cv2
	center = 320
	source = 1


	base = Base()
	if base.find_arduino() is False:
		print("Cannot connect to arduino")
		return 

	cam = cv2.VideoCapture(source)
	if cam is None or not cam.isOpened():
       print('Warning: unable to open video source: ', source)	
       return

	pid = PID(kp, kd, ki, min, max)

	while True:
		ret, frame = cam.read()
		if not ret:
			break
		gray = cv2.cvtColor(frame, cv2.BGR2GRAY)
		val = get_signature(frame)
		err = center - val
		result = pid.calculate(err)
		if err > 0:			
			result = pid.calculate(err)
			base.set_motor(ac.MOTOR_L, ac.FORWARD, ac.MAXPOWER - result)
			base.set_motor(ac.MOTOR_R, ac.FORWARD, ac.MAXPOWER)
		else:
			result = pid.calculate(-err)
			base.set_motor(ac.MOTOR_L, ac.FORWARD, ac.MAXPOWER)
			base.set_motor(ac.MOTOR_R, ac.FORWARD, ac.MAXPOWER - result)

main()
