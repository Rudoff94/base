from base import Base
#from constant import ArduinoCommand as ac
from time import sleep
from detect_black_object import get_signature
from pid import PID
import cv2
import numpy as np

def main():
	#Variables for PID
	
	kp = 1
	kd = 0.5
	ki = 0
	
	min = 0
	max = 255

	#Variables for cv2
	center = 320
	source = 2

	red = (0,0,255)
	green = (0,255,0)
	thinkness = 3
	center_x = (center, 480) 
	center_end = (center, 0)

	'''
	base = Base()
	if base.find_arduino() is False:
		print("Cannot connect to arduino")
		return 
	'''

	cam = cv2.VideoCapture(source)
	if cam is None or not cam.isOpened():
		print("Warning: unable to open video source:")
		return 

	pid = PID(kp, kd, ki, min, max)

	while True:
		ret, frame = cam.read()
		if not ret:
			break

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		index = get_signature(gray)

		frame = cv2.line(frame, center_x, center_end, green, thinkness)
		
		if index == None:
			print("Black line is not detected")
			#base.set_motor(ac.MOTOR_L, ac.FORWARD, ac.MINPOWER)
			#base.set_motor(ac.MOTOR_R, ac.FORWARD, ac.MINPOWER)
			
		else:
			start_point = (index, frame.shape[0])
			end_point = (index, 0)
			frame = cv2.line(frame, start_point, end_point, red, thinkness)
			err = center - index
			if err > 0:			
				result = pid.calculate(err)
				print("Left: ", result)
				#base.set_motor(ac.MOTOR_L, ac.FORWARD, ac.MAXPOWER - result)
				#base.set_motor(ac.MOTOR_R, ac.FORWARD, ac.MAXPOWER)
			else:
				result = pid.calculate(-err)
				print("Right:", result)
				#base.set_motor(ac.MOTOR_L, ac.FORWARD, ac.MAXPOWER)
				#base.set_motor(ac.MOTOR_R, ac.FORWARD, ac.MAXPOWER - result)
		cv2.imshow("Video", frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break 

		
	cv2.destroyAllWindows()

main()	
