import cv2
import numpy as np
from time import sleep
import matplotlib.pyplot as plt

def get_signature(frame):
	last_result = np.linalg.norm(frame[:, 0])
	cur_result = 0
	
	min = np.linalg.norm(frame[:, 1]) - last_result
	max = np.linalg.norm(frame[:, 1]) - last_result

	index_min = 0
	index_max = 0
	
	lenOfVector = []
	dif = []
	
	for index in range(1, frame.shape[1]):
		cur_result = np.linalg.norm(frame[:, index])

		lenOfVector.append(cur_result)
		dif.append((cur_result - last_result))

		if dif [-1] < min: 
			min = dif[-1]
			index_min = index

		if dif [-1] > max: 
			max = dif[-1]
			index_max = index

		last_result = cur_result
	index = (index_max + index_min) // 2
	print(min, index_max)
	return dif, lenOfVector, index






def get_signature_2(frame):
	last_result = np.linalg.norm(frame[:, 0])
	cur_result = 0
	
	min = np.linalg.norm(frame[:, 1]) - last_result
	max = np.linalg.norm(frame[:, 1]) - last_result

	index_min = 0
	index_max = 0
	
	lenOfVector = []
	dif = []
	
	for index in range(1, frame.shape[1]):
		cur_result = np.linalg.norm(frame[:, index])

		lenOfVector.append(cur_result)
		dif.append((cur_result - last_result))

		if dif [-1] < min: 
			min = dif[-1]
			index_min = index

		if dif [-1] > max: 
			max = dif[-1]
			index_max = index

		last_result = cur_result
	if index_min < index_max:
		print("Line is black")
		index = (index_max + index_min) // 2
		print(min, index_max)
		return dif, lenOfVector, index		
	else:
		return None
		







def detect_black(frame, threshold):
	#1 - обрезать кадр, оставить только нижнюю часть
	first_x = 0
	second_x = 640
	#lenOfVector = []

	cut_frame = frame[380: , :] #1-st Строки 2-nd Столбцы

	for index in range(cut_frame.shape[1]):
		result = np.linalg.norm(cut_frame[:, index])
		#lenOfVector.append(result)
		if result < threshold:
			first_x = index
			break

	for index in range(first_x, cut_frame.shape[1]):
		result = np.linalg.norm(cut_frame[:, index])	
		#lst.append(result)
		if result > threshold:
			second_x = index
			break

	result = (second_x + first_x) // 2
	return result
	#, lenOfVector

			


def main():
	#cam = cv2.VideoCapture(1)	
	color = (0, 255, 0)
	thinkness = 3

	threshold = 4500
	img = cv2.imread("WhiteLine.png", 0)
#	cv2.imshow("image", img)
	#x = detect_black(img, threshold)
	value = get_signature_2(img)

	if value == None:
		print("No black line detected")
		return
	else:
		dif, len_of_vector, index = value


	cord_x = [i for i in range(len(len_of_vector))]

	
	#Отрисовка графиков	

	#plt.plot(cord_x, len_of_vector)
	plt.plot(cord_x, dif)
	plt.show()
	

	#Координаты линии
	start_point = (index, img.shape[0])
	end_point = (index, 0)


	img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
	img = cv2.line(img, start_point, end_point, color, thinkness)
	

	cv2.imshow("image", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return

	
	#while True:

	#	ret, frame = cam.read()

		#if not ret:
		#	break

	#	gray = cv2.cvtColor(frame, cv2.BGR2GRAY)







if __name__ == "__main__":
	main()